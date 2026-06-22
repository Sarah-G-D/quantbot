# main_live.py
import time
import json
import os
import requests
import pandas as pd
import numpy as np
import MetaTrader5 as mt5
import logfire
from datetime import datetime, timedelta, timezone  # Uses pure standard library
from alpha_agent import FiveBotAlphaCouncil
from risk_agent import AssetRiskGuard, AccountState

# Configure Logfire for live monitoring
logfire.configure(
    token="pylf_v1_eu_zwcrVr8W6Lq9FYfGFLcbP1kr3VmcL6kyJdTqpbZNNhMp",
    console=logfire.ConsoleOptions(min_log_level="notice")
)
logfire.instrument_pydantic()

ALLOWED_ASSETS = [
    "AUDUSD", "EURCHF", "EURGBP", "EURUSD", "GBPUSD", "USDCAD", "USDCHF", "USDJPY",
    "XAGUSD", "XAUUSD",
    "BARUSD", "BTCUSD", "ETHUSD", "SOLUSD", "XRPUSD"
]

# ---------------------------------------------------------------------------
# SENTIMENT CONFIGURATION (Bypassed for safe launch)
# ---------------------------------------------------------------------------
def load_sentiment_bias() -> str:
    """Returns 'NEUTRAL' instantly to protect the execution loop from timeout delays."""
    return "NEUTRAL"
# ---------------------------------------------------------------------------

def get_current_bst_time() -> datetime:
    """Returns current BST (London) time using pure standard library (no pytz required)."""
    # BST in June is UTC + 1 hour
    utc_now = datetime.now(timezone.utc)
    return utc_now + timedelta(hours=1)

def get_symbol_filling_mode(symbol: str) -> int:
    """Dynamically queries the MT5 terminal for the broker's supported filling mode."""
    info = mt5.symbol_info(symbol)
    if info is None:
        return mt5.ORDER_FILLING_FOK  # Fallback
    
    # Check bitmask flags for supported modes
    if (info.filling_mode & 1) != 0: 
        return mt5.ORDER_FILLING_FOK
    elif (info.filling_mode & 2) != 0: 
        return mt5.ORDER_FILLING_IOC
    else:
        return mt5.ORDER_FILLING_RETURN

def calculate_mt5_lot_size(symbol: str, trade_size_cash: float, mid_price: float) -> float:
    """Calculates MT5 lot size using dynamic contract size and volume limits."""
    info = mt5.symbol_info(symbol)
    if info is None:
        return 0.0
    
    # Get the contract size (e.g., 100,000 for Forex, 100 for Gold, 1 for BTC)
    contract_size = info.trade_contract_size
    
    # Calculate target units required
    target_units = trade_size_cash / mid_price
    
    # Convert units to lots based on the contract size of the asset
    raw_lots = target_units / contract_size
    
    # Respect MT5 broker volume steps and limits
    lot_step = info.volume_step if info.volume_step > 0 else 0.01
    min_lot = info.volume_min if info.volume_min > 0 else 0.01
    max_lot = info.volume_max if info.volume_max > 0 else 100.0
    
    # Round down to the nearest allowed lot step
    lots = round(raw_lots / lot_step) * lot_step
    lots = max(min_lot, min(max_lot, lots))
    
    return round(lots, 2)

def get_live_book_imbalance(symbol: str) -> float:
    """Fetches Depth of Market from MT5 to compute a live order book imbalance."""
    items = mt5.market_book_get(symbol)
    if not items or len(items) == 0:
        return 0.0
    
    total_bids = 0.0
    total_asks = 0.0
    
    for item in items:
        if item.type in [mt5.BOOK_TYPE_BUY, mt5.BOOK_TYPE_BUY_MARKET]:
            total_bids += item.volume_dbl if hasattr(item, 'volume_dbl') else item.volume
        elif item.type in [mt5.BOOK_TYPE_SELL, mt5.BOOK_TYPE_SELL_MARKET]:
            total_asks += item.volume_dbl if hasattr(item, 'volume_dbl') else item.volume
            
    if (total_bids + total_asks) > 0:
        return (total_bids - total_asks) / (total_bids + total_asks)
    return 0.0

def warmup_council_histories(council: FiveBotAlphaCouncil):
    """Fills history with the latest M1 close bars to avoid waiting for initial warmups."""
    print("⏳ Warming up asset price histories using MT5 M1 bars...")
    for symbol in ALLOWED_ASSETS:
        rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M1, 0, 100)
        if rates is not None and len(rates) > 0:
            prices = [float(candle['close']) for candle in rates]
            council.price_histories[symbol] = prices
            print(f"   Warmup complete for {symbol}: Loaded {len(prices)} bars.")
        else:
            print(f"   ⚠️ Warmup skipped/failed for {symbol}. Will accumulate live ticks.")

def execute_mt5_order(symbol: str, action: str, volume: float, price: float, comment: str = ""):
    """Submits a market execution order directly to the MetaTrader 5 terminal."""
    order_type = mt5.ORDER_TYPE_BUY if action == "BUY" else mt5.ORDER_TYPE_SELL
    
    filling_mode = get_symbol_filling_mode(symbol)
    
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "type": order_type,
        "price": price,
        "deviation": 20, 
        "magic": 123456, 
        "comment": comment,
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": filling_mode,
    }
    
    result = mt5.order_send(request)
    if result is None:
         print(f"❌ MT5 Order Failed: order_send returned None for {symbol}")
         return None

    if result.retcode != mt5.TRADE_RETCODE_DONE:
        logfire.error("MT5 Order Failed", symbol=symbol, action=action, error=result.comment, retcode=result.retcode)
        print(f"❌ MT5 Order Failed for {symbol}: Retcode {result.retcode} - {result.comment}")
    else:
        logfire.notice("MT5 Order Executed Successfully", symbol=symbol, action=action, price=result.price, volume=volume)
        print(f"🎯 Successful {action} order executed on {symbol} at {result.price}")
    return result

def live_trading_loop():
    print("==================================================")
    print("      QUANTBOT METATRADER 5 LIVE ORCHESTRATOR     ")
    print("==================================================")
    
    if not mt5.initialize():
        print(f"❌ MT5 Initialization failed: {mt5.last_error()}")
        return
        
    print("✅ Successfully linked to MetaTrader 5 terminal.")
    
    council = FiveBotAlphaCouncil()
    guard = AssetRiskGuard()
    
    warmup_council_histories(council)
    
    # Subscribe to Depth of Market books
    for symbol in ALLOWED_ASSETS:
        if mt5.market_book_add(symbol):
            print(f"✅ Subscribed to order book depth for {symbol}")
        else:
            print(f"⚠️ Failed to subscribe to order book depth for {symbol}: {mt5.last_error()}")
    
    try:
        while True:
            # ---------------------------------------------------------------------------
            # SAFEGUARD: AUTO-FLAT 21:45 BST END-OF-ROUND RULE
            # ---------------------------------------------------------------------------
            now_bst = get_current_bst_time()
            if now_bst.hour == 21 and now_bst.minute >= 45:
                # Check if we have active positions to close
                active_positions = mt5.positions_get()
                if active_positions and len(active_positions) > 0:
                    print("🕒 Approaching Round 1 Cutoff (22:00 BST). Flattening all positions to lock in rank...")
                    for pos in active_positions:
                        symbol = pos.symbol
                        direction = "BUY" if pos.type == mt5.POSITION_TYPE_BUY else "SELL"
                        close_action = "SELL" if direction == "BUY" else "BUY"
                        tick = mt5.symbol_info_tick(symbol)
                        if tick is not None:
                            close_price = tick.bid if direction == "BUY" else tick.ask
                            execute_mt5_order(symbol, close_action, pos.volume, close_price, comment="Cutoff Flat")
                    print("✅ All positions flattened. Standing secured for Round 1 snapshot.")
                time.sleep(5)
                continue
            # ---------------------------------------------------------------------------

            sentiment_bias = load_sentiment_bias()
            
            # Apply sentiment skew directly to strategy properties inside the council
            if sentiment_bias == "BULLISH":
                council.bot1.threshold = 0.25 
                council.bot3.z_threshold = 2.8 
            elif sentiment_bias == "BEARISH":
                council.bot1.threshold = 0.45 
                council.bot3.z_threshold = 2.2 
            else:
                council.bot1.threshold = 0.35 
                council.bot3.z_threshold = 2.5 
            
            acct = mt5.account_info()
            if acct is None:
                print("⚠️ Failed to fetch live account details from MT5.")
                time.sleep(1)
                continue
                
            current_state = AccountState(
                equity=acct.equity,
                used_margin=acct.margin,
                gross_exposure=acct.margin_initial 
            )
            
            for symbol in ALLOWED_ASSETS:
                tick = mt5.symbol_info_tick(symbol)
                if tick is None:
                    continue
                    
                mid_price = (tick.bid + tick.ask) / 2.0
                council.update_price(symbol, mid_price)
                
                positions = mt5.positions_get(symbol=symbol)
                
                # --- EXIT EVALUATION ---
                if positions:
                    pos = positions[0] 
                    entry_price = pos.price_open
                    direction = "BUY" if pos.type == mt5.POSITION_TYPE_BUY else "SELL"
                    
                    # Calculate correct percentage return based on executable order book sides
                    if direction == "BUY":
                        current_return = (tick.bid - entry_price) / entry_price
                    else:
                        current_return = (entry_price - tick.ask) / entry_price
                        
                    # Calculate live book imbalance to evaluate the current council consensus
                    live_imbalance = get_live_book_imbalance(symbol)
                    mock_row = {
                        'bid': tick.bid,
                        'ask': tick.ask,
                        'book_imbalance': live_imbalance,
                    }
                    analysis = council.evaluate_market(mock_row, symbol)
                    signal = analysis.get("signal")
                    
                    # Stateful reversal exit trigger
                    reversal_triggered = (direction == "BUY" and signal == "SELL") or (direction == "SELL" and signal == "BUY")
                    
                    # Exit if brackets hit OR if council votes against us
                    if current_return >= 0.010 or current_return <= -0.005 or reversal_triggered:
                        close_action = "SELL" if direction == "BUY" else "BUY"
                        close_price = tick.bid if direction == "BUY" else tick.ask
                        reason = "Exit Bracket" if not reversal_triggered else "Council Reversal"
                        print(f"🛑 [Exit Signal] Closing {symbol} position due to {reason}...")
                        execute_mt5_order(symbol, close_action, pos.volume, close_price, comment=reason)
                        
                # --- ENTRY EVALUATION ---
                else:
                    live_imbalance = get_live_book_imbalance(symbol)
                    
                    mock_row = {
                        'bid': tick.bid,
                        'ask': tick.ask,
                        'book_imbalance': live_imbalance,
                    }
                    
                    analysis = council.evaluate_market(mock_row, symbol)
                    signal = analysis.get("signal")
                    
                    if signal in ["BUY", "SELL"]:
                        trade_size_cash = 1000000.0 
                        
                        current_time = pd.Timestamp.now()
                        is_safe = guard.validate_trade(current_state, symbol, trade_size_cash, current_time)
                        
                        if is_safe:
                            # Use new dynamic lot calculation
                            mt5_lot_size = calculate_mt5_lot_size(symbol, trade_size_cash, mid_price)
                            
                            if mt5_lot_size > 0:
                                print(f"🚀 [Entry Signal] Executing {signal} for {symbol} with lots {mt5_lot_size}...")
                                entry_price_exec = tick.ask if signal == "BUY" else tick.bid
                                execute_mt5_order(symbol, signal, mt5_lot_size, entry_price_exec, comment="Council Consensus")
            
            # Control loop frequency
            time.sleep(1) 
            
    except KeyboardInterrupt:
        print("\nStopping Live Execution Bridge...")
    finally:
        for symbol in ALLOWED_ASSETS:
            mt5.market_book_release(symbol)
        mt5.shutdown()
        print("MetaTrader 5 connection closed.")

if __name__ == "__main__":
    live_trading_loop()