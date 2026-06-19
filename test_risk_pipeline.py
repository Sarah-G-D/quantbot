import pandas as pd
from datetime import datetime
from risk_agent import AccountState, AssetRiskGuard

def run_risk_agent_simulation():
    print("=== INITIALIZING PLATFORM RISK ENGINE SIMULATION ===")

    # 1. Initialize Pydantic Account State
    account = AccountState(
        equity=1000000.0,
        used_margin=0.0,
        gross_exposure=0.0,
        asset_exposures={
            "EURUSD": 0.0, "BTCUSD": 0.0, "XAUUSD": 0.0, "AUDUSD": 0.0
        }
    )
    
    guard = AssetRiskGuard()

    # --- TEST 1: Basic Valid Forex Trade ---
    print("\n--- TEST 1: Requesting Standard EURUSD Entry ---")
    timestamp_1 = "2026-06-22 10:00:00"
    trade_size_1 = 1000000.0
    
    is_approved_1 = guard.validate_trade(
        account=account,
        asset="EURUSD",
        trade_size=trade_size_1,
        current_time_str=timestamp_1
    )
    
    if is_approved_1:
        account.gross_exposure += trade_size_1
        account.asset_exposures["EURUSD"] = trade_size_1
        account.used_margin += (trade_size_1 * 0.0333)
        print("💰 Account State Updated successfully.")

    # --- TEST 2: Internal Safety Cap Violation ---
    print("\n--- TEST 2: Requesting Aggressive BTCUSD Size ---")
    timestamp_2 = "2026-06-22 14:30:00"
    trade_size_2 = 3000000.0 
    
    is_approved_2 = guard.validate_trade(
        account=account,
        asset="BTCUSD",
        trade_size=trade_size_2,
        current_time_str=timestamp_2
    )
    if not is_approved_2:
        print("🛡️ Guard successfully blocked excessive Crypto allocation.")

    # --- TEST 3: Section 15 Pre-Snapshot Daily Entry Ban ---
    print("\n--- TEST 3: Requesting Order Execution Right Before Snapshot ---")
    timestamp_3 = "2026-06-22 21:52:00"
    trade_size_3 = 500000.0
    
    is_approved_3 = guard.validate_trade(
        account=account,
        asset="AUDUSD",
        trade_size=trade_size_3,
        current_time_str=timestamp_3
    )
    if not is_approved_3:
        print("🛡️ Guard successfully blocked thin liquidity entry.")

    # --- TEST 4: The 21:55 Daily Hard Flatten Signal ---
    print("\n--- TEST 4: Evaluating the 21:55 Daily Hard Flatten Trigger ---")
    timestamp_4 = datetime(2026, 6, 22, 21, 56, 0)
    
    kill_list, is_hard_flatten = guard.monitor_compliance_clocks(account, timestamp_4)
    
    if is_hard_flatten and kill_list:
        print(f"🛑 Hard Flatten Active! Closing: {kill_list}")
        for asset in kill_list:
            account.asset_exposures[asset] = 0.0
        account.gross_exposure = 0.0
        account.used_margin = 0.0
        guard.register_completed_trade()
        print("🧼 Portfolio successfully flattened into cash.")

    # --- TEST 5: Section 17 Sharpe Side-Prize Verification ---
    print("\n--- TEST 5: Checking Progress for $10,000 Sharpe Prize ---")
    day_idx = 3
    total_rounds_days = 5
    
    opt_forex = guard.get_optimized_size("FOREX", day_idx, total_rounds_days)
    opt_crypto = guard.get_optimized_size("CRYPTO", day_idx, total_rounds_days)
    
    print(f"📈 Completed Trades: {guard.total_completed_trades} / 30")
    print(f"⚙️ Target sizing -> Forex: ${opt_forex:,.2f} | Crypto: ${opt_crypto:,.2f}")
    print("\n=== SIMULATION TESTS COMPLETE: RISK AGENT READY ===")

if __name__ == "__main__":
    run_risk_agent_simulation()