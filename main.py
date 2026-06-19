import os
import glob
import pandas as pd
import numpy as np
import logfire
from alpha_agent import FiveBotAlphaCouncil
from risk_agent import AssetRiskGuard, AccountState

# ==============================================================================
# PERFORMANCE CONFIGURATION
# Set to 10 for high resolution. Increase to 50 or 100 if your computer runs out of RAM.
# ==============================================================================
DOWNSAMPLE_STEP = 100

# Configure Logfire
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

def load_and_preprocess_file(file_path: str, asset_name: str, downsample_step: int, params: dict = None) -> pd.DataFrame:
    """
    Optimized loader: Filters provider and downsamples IMMEDIATELY.
    Calculates technical features vectorized across the series before looping.
    """
    try:
        raw_df = pd.read_parquet(file_path, engine='pyarrow')
    except Exception:
        return None
    if raw_df.empty:
        return None
        
    df_cleaned = raw_df[raw_df['provider'] == 'XSMM01CH01'].copy()
    if df_cleaned.empty:
        return None
        
    # Downsample immediately to reduce raw row processing load
    df_down = df_cleaned.iloc[::downsample_step].copy()
    
    # Process 5-tier level arrays
    for i in range(5):
        try:
            df_down[f'bid_price_lvl_{i+1}'] = df_down['bidprices'].str[i].astype(float)
            df_down[f'bid_size_lvl_{i+1}']  = df_down['bidsizes'].str[i].astype(float)
            df_down[f'ask_price_lvl_{i+1}'] = df_down['askprices'].str[i].astype(float)
            df_down[f'ask_size_lvl_{i+1}']  = df_down['asksizes'].str[i].astype(float)
        except Exception:
            # Fallback values if level values are missing
            df_down[f'bid_price_lvl_{i+1}'] = np.nan
            df_down[f'bid_size_lvl_{i+1}']  = 0.0
            df_down[f'ask_price_lvl_{i+1}'] = np.nan
            df_down[f'ask_size_lvl_{i+1}']  = 0.0
            
    total_bid_depth = df_down[[f'bid_size_lvl_{j}' for j in range(1, 6)]].sum(axis=1)
    total_ask_depth = df_down[[f'ask_size_lvl_{j}' for j in range(1, 6)]].sum(axis=1)
    df_down['book_imbalance'] = (total_bid_depth - total_ask_depth) / (total_bid_depth + total_ask_depth + 1e-8)
    
    df_down['assigned_symbol'] = asset_name
    df_down['mid_price'] = (df_down['bid'].astype(float) + df_down['ask'].astype(float)) / 2.0
    
    # Extract operational parameter overrides
    bot1_thresh = params.get("bot1_threshold", 0.35) if params else 0.35
    bot3_thresh = params.get("bot3_z_threshold", 2.5) if params else 2.5
    
    # Pre-calculate Bot 1 Signals
    df_down['bot1_vote'] = 'HOLD'
    df_down.loc[df_down['book_imbalance'] > bot1_thresh, 'bot1_vote'] = 'BUY'
    df_down.loc[df_down['book_imbalance'] < -bot1_thresh, 'bot1_vote'] = 'SELL'
    
    # Pre-calculate Bot 2 Signals
    fast_ma_2 = df_down['mid_price'].rolling(5, min_periods=5).mean()
    slow_ma_2 = df_down['mid_price'].rolling(15, min_periods=15).mean()
    recent_std_2 = df_down['mid_price'].rolling(20, min_periods=20).std().fillna(0)
    prev_std_2 = recent_std_2.shift(1).fillna(0)
    
    df_down['bot2_vote'] = 'HOLD'
    vol_expansion = recent_std_2 > prev_std_2
    df_down.loc[vol_expansion & (fast_ma_2 > slow_ma_2), 'bot2_vote'] = 'BUY'
    df_down.loc[vol_expansion & (fast_ma_2 < slow_ma_2), 'bot2_vote'] = 'SELL'
    
    # Pre-calculate Bot 3 Signals
    mean_30 = df_down['mid_price'].rolling(30, min_periods=30).mean()
    std_30 = df_down['mid_price'].rolling(30, min_periods=30).std().fillna(0)
    std_30_safe = std_30.replace(0, 1e-8)
    z_score = (df_down['mid_price'] - mean_30) / std_30_safe
    
    df_down['bot3_vote'] = 'HOLD'
    df_down.loc[z_score < -bot3_thresh, 'bot3_vote'] = 'BUY'
    df_down.loc[z_score > bot3_thresh, 'bot3_vote'] = 'SELL'
    
    # Pre-calculate Bot 4 Signals
    fast_ma_4 = df_down['mid_price'].rolling(10, min_periods=10).mean()
    slow_ma_4 = df_down['mid_price'].rolling(30, min_periods=30).mean()
    
    df_down['bot4_vote'] = 'HOLD'
    df_down.loc[fast_ma_4 > slow_ma_4, 'bot4_vote'] = 'BUY'
    df_down.loc[fast_ma_4 < slow_ma_4, 'bot4_vote'] = 'SELL'
    
    return df_down

def get_sorted_trading_days(data_dir: str) -> list:
    all_files = glob.glob(os.path.join(data_dir, "*.parquet"))
    unique_dates = set()
    for f in all_files:
        base = os.path.basename(f)
        # Fixes split pattern typo from previous script
        parts = base.replace(".parquet", "").split("_")
        if len(parts) >= 4:
            date_str = f"{parts[-3]}_{parts[-2]}_{parts[-1]}"
            unique_dates.add(date_str)
    return sorted(list(unique_dates))

# ==========================================
# 3. BACKTEST RUNNER (COMPOSITE METRIC ENGINE)
# ==========================================

def run_backtest_on_days(target_days: list, data_dir: str, council_params: dict = None) -> dict:
    council = FiveBotAlphaCouncil()
    guard = AssetRiskGuard()
    my_account = AccountState(equity=1000000.0, used_margin=0.0, gross_exposure=0.0)
    initial_equity = my_account.equity
    
    portfolio_positions = {asset: None for asset in ALLOWED_ASSETS}
    trade_size_cash = 1000000.0
    all_files = sorted(glob.glob(os.path.join(data_dir, "*.parquet")))
    
    for target_day in target_days:
        print(f"     Processing market data for day: {target_day}...", flush=True)
        day_files = [f for f in all_files if target_day in f]
        day_dfs = []
        
        for file_path in day_files:
            file_name = os.path.basename(file_path)
            asset_name = next((a for a in ALLOWED_ASSETS if a in file_name.replace("_", "")), None)
            if not asset_name:
                continue
            
            df_clean = load_and_preprocess_file(file_path, asset_name, DOWNSAMPLE_STEP, council_params)
            if df_clean is not None and not df_clean.empty:
                day_dfs.append(df_clean)

        if not day_dfs:
            continue
            
        master_day_stream = pd.concat(day_dfs, axis=0, ignore_index=True)
        master_day_stream['time'] = pd.to_datetime(master_day_stream['time'])
        master_day_stream = master_day_stream.sort_values(by='time').reset_index(drop=True)
        
        # Fast streaming loop
        for _, row in master_day_stream.iterrows():
            symbol = row['assigned_symbol']
            mid_price = row['mid_price']
            
            # Maintain real-time price state for lead-lag checks
            council.update_price(symbol, mid_price)
            
            # Continuously monitor compliance and drawdown metrics [1]
            guard.evaluate_compliance_violations(my_account, row['time'])
            
            active_trade = portfolio_positions[symbol]
            
            # --- EVALUATE EXITS ---
            if active_trade is not None:
                current_pnl = active_trade['pos_size'] * (mid_price - active_trade['entry_price'])
                my_account.equity = initial_equity + current_pnl
                
                direction_mult = 1 if active_trade['direction'] == "BUY" else -1
                current_return = direction_mult * (mid_price - active_trade['entry_price']) / active_trade['entry_price']
                
                if current_return >= 0.002 or current_return <= -0.001:
                    initial_equity += current_pnl
                    my_account.equity = initial_equity
                    my_account.gross_exposure -= trade_size_cash
                    portfolio_positions[symbol] = None
                    continue

            # --- EVALUATE ENTRIES ---
            if portfolio_positions[symbol] is None:
                if not guard.is_session_liquid(symbol, row['time']):
                    continue
                    
                analysis = council.evaluate_market(row, symbol)
                signal = analysis.get("signal")
                
                if signal in ["BUY", "SELL"]:
                    is_safe = guard.validate_trade(my_account, symbol, trade_size_cash, row['time'])
                    if is_safe:
                        pos_size = (trade_size_cash / mid_price) if signal == "BUY" else -(trade_size_cash / mid_price)
                        portfolio_positions[symbol] = {
                            'entry_price': mid_price,
                            'pos_size': pos_size,
                            'direction': signal
                        }
                        my_account.gross_exposure += trade_size_cash
                        
    total_return = (my_account.equity - 1000000.0) / 1000000.0
    sharpe = guard.get_sharpe_ratio()
    
    return {
        "total_return": total_return,
        "max_drawdown": guard.max_drawdown,
        "sharpe_ratio": sharpe,
        "risk_discipline": guard.risk_discipline_score
    }

# ==========================================
# 4. SURROGATE SCORING FUNCTION
# ==========================================

def calculate_surrogate_score(metrics: dict) -> float:
    ret = metrics["total_return"]
    dd = metrics["max_drawdown"]
    sharpe = metrics["sharpe_ratio"]
    risk = metrics["risk_discipline"]
    
    s_return = min(100.0, max(0.0, (ret / 0.05) * 100.0))
    s_drawdown = max(0.0, 100.0 - (dd / 0.14) * 100.0) 
    s_sharpe = min(100.0, max(0.0, (sharpe / 1.5) * 100.0))
    s_risk = risk 
    
    composite_score = (0.70 * s_return) + (0.15 * s_drawdown) + (0.10 * s_sharpe) + (0.05 * s_risk)
    return composite_score

# ==========================================
# 5. CROSS-VALIDATION ORCHESTRATION
# ==========================================

def run_cross_validation(data_dir: str):
    trading_days = get_sorted_trading_days(data_dir)
    num_days = len(trading_days)
    
    if num_days < 15:
        print("Error: Insufficient trading data to run walk-forward validation.")
        return
        
    print(f"Parsed {num_days} unique trading days.")
    
    fold1_train = trading_days[0:14]
    fold1_test = trading_days[14:21]
    
    fold2_train = trading_days[0:21]
    fold2_test = trading_days[21:]
    
    param_grid = [
        {"bot1_threshold": 0.35, "bot3_z_threshold": 2.0},
        {"bot1_threshold": 0.45, "bot3_z_threshold": 2.5}
    ]
    
    oos_results = []
    
    # --- FOLD 1 ---
    print("\n--- Running Fold 1 Training (Composite Score Search) ---")
    best_f1_params = None
    best_f1_score = -999.0
    
    for params in param_grid:
        metrics = run_backtest_on_days(fold1_train, data_dir, council_params=params)
        score = calculate_surrogate_score(metrics)
        print(f"Params: {params} | OOS Surrogate Score: {score:.2f} | (Ret: {metrics['total_return']*100:.2f}%, DD: {metrics['max_drawdown']*100:.2f}%, Sharpe: {metrics['sharpe_ratio']:.3f}, Risk: {metrics['risk_discipline']})")
        if score > best_f1_score:
            best_f1_score = score
            best_f1_params = params
            
    print(f"Fold 1 Optimal Params: {best_f1_params}")
    f1_test_res = run_backtest_on_days(fold1_test, data_dir, council_params=best_f1_params)
    f1_test_score = calculate_surrogate_score(f1_test_res)
    oos_results.append(f1_test_res)
    print(f"Fold 1 OOS Result -> Surrogate Score: {f1_test_score:.2f} | Return: {f1_test_res['total_return']*100:.2f}% | MaxDD: {f1_test_res['max_drawdown']*100:.2f}%")

    # --- FOLD 2 ---
    print("\n--- Running Fold 2 Training (Composite Score Search) ---")
    best_f2_params = None
    best_f2_score = -999.0
    
    for params in param_grid:
        metrics = run_backtest_on_days(fold2_train, data_dir, council_params=params)
        score = calculate_surrogate_score(metrics)
        print(f"Params: {params} | OOS Surrogate Score: {score:.2f} | (Ret: {metrics['total_return']*100:.2f}%, DD: {metrics['max_drawdown']*100:.2f}%, Sharpe: {metrics['sharpe_ratio']:.3f}, Risk: {metrics['risk_discipline']})")
        if score > best_f2_score:
            best_f2_score = score
            best_f2_params = params
            
    print(f"Fold 2 Optimal Params: {best_f2_params}")
    f2_test_res = run_backtest_on_days(fold2_test, data_dir, council_params=best_f2_params)
    f2_test_score = calculate_surrogate_score(f2_test_res)
    oos_results.append(f2_test_res)
    print(f"Fold 2 OOS Result -> Surrogate Score: {f2_test_score:.2f} | Return: {f2_test_res['total_return']*100:.2f}% | MaxDD: {f2_test_res['max_drawdown']*100:.2f}%")

    # --- AGGREGATE EVALUATION ---
    avg_oos_return = np.mean([r['total_return'] for r in oos_results])
    avg_oos_drawdown = np.mean([r['max_drawdown'] for r in oos_results])
    avg_oos_sharpe = np.mean([r['sharpe_ratio'] for r in oos_results])
    avg_oos_risk = np.mean([r['risk_discipline'] for r in oos_results])
    
    final_aggregate_metrics = {
        "total_return": avg_oos_return,
        "max_drawdown": avg_oos_drawdown,
        "sharpe_ratio": avg_oos_sharpe,
        "risk_discipline": avg_oos_risk
    }
    final_aggregate_score = calculate_surrogate_score(final_aggregate_metrics)
    
    print("\n==============================================")
    print("      WALK-FORWARD COMPOSITE OOS SUMMARY      ")
    print("==============================================")
    print(f"Overall Walk-Forward Score: {final_aggregate_score:.2f} / 100.00")
    print(f"Average Out-of-Sample Return: {avg_oos_return*100:.2f}%")
    print(f"Average Out-of-Sample Max Drawdown: {avg_oos_drawdown*100:.2f}%")
    print(f"Average Out-of-Sample Sharpe Ratio: {avg_oos_sharpe:.4f}")
    print(f"Average Out-of-Sample Risk Score: {avg_oos_risk:.1f} / 100")
    print("==============================================")

if __name__ == "__main__":
    DATA_DIRECTORY = "pricer-output-2026-05-11_2026-06-10"
    run_cross_validation(DATA_DIRECTORY)