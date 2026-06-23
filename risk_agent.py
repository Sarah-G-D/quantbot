import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time
from pydantic import BaseModel, Field

def calculate_standalone_sharpe(equity_list) -> float:
    if len(equity_list) < 8:
        return 0.0
    returns = []
    for i in range(1, len(equity_list)):
        prev = equity_list[i-1]
        curr = equity_list[i]
        if prev <= 0:
            returns.append(0.0)
        else:
            returns.append((curr - prev) / prev)
    std_dev = np.std(returns)
    if std_dev == 0:
        return 0.0
    return float(np.mean(returns) / std_dev)

class AccountState(BaseModel):
    equity: float
    used_margin: float = 0.0
    gross_exposure: float = 0.0
    asset_exposures: dict[str, float] = Field(default_factory=dict)

class AssetRiskGuard:
    def __init__(self):
        self.MAX_LEVERAGE_GLOBAL = 30.0        
        self.STOP_OUT_LEVEL = 0.30       
        self.HARD_DRAWDOWN_LIMIT = 0.14  
        self.margin_rates = {"FOREX": 0.0333, "METALS": 0.0500, "CRYPTO": 0.2000}
        
        self.max_leverage_limits = {
            "BTCUSD": 2.0, "ETHUSD": 2.0, "SOLUSD": 2.0, "XRPUSD": 2.0, "BARUSD": 2.0,
            "XAUUSD": 5.0, "XAGUSD": 5.0, "FOREX": 5.0
        }
        
        self.peak_equity = 1000000.0
        self.max_drawdown = 0.0
        self.risk_discipline_score = 100.0
        
        self.margin_90_start = None
        self.margin_95_start = None
        self.margin_98_start = None
        
        self.leverage_28_start = None
        self.leverage_29_start = None
        self.leverage_30_start = None
        
        self.concentration_90_start = None
        self.deductions_applied = set()
        
        self.equity_history_15m = []
        self.last_sharpe_time = None
        self.total_completed_trades = 0
        self.REQUIRED_TRADES_FOR_PRIZE = 30
        self.MAX_RPS = 450.0  
        self.request_timestamps = []

    def check_rate_limit(self) -> bool:
        now = time.time()
        self.request_timestamps = [t for t in self.request_timestamps if now - t < 1.0]
        if len(self.request_timestamps) >= self.MAX_RPS:
            return False
        self.request_timestamps.append(now)
        return True

    def is_session_liquid(self, symbol: str, current_time) -> bool:
        if any(crypto in symbol for crypto in ["BTC", "ETH", "SOL", "XRP", "BAR"]):
            return True
        hour = current_time.hour
        if 21 <= hour < 23:
            return False
        return True

    def calculate_metrics(self, account: AccountState, current_time):
        if account.equity > self.peak_equity:
            self.peak_equity = account.equity
            
        current_dd = (self.peak_equity - account.equity) / self.peak_equity if self.peak_equity > 0 else 0.0
        if current_dd > self.max_drawdown:
            self.max_drawdown = current_dd
            
        leverage = account.gross_exposure / account.equity if account.equity > 0 else 0.0
        margin_usage = account.used_margin / account.equity if account.equity > 0 else 0.0
        
        if self.last_sharpe_time is None or (current_time - self.last_sharpe_time) >= timedelta(minutes=15):
            self.equity_history_15m.append(account.equity)
            self.last_sharpe_time = current_time
            
        return current_dd, leverage, margin_usage

    def evaluate_compliance_violations(self, account: AccountState, current_time):
        drawdown, leverage, margin_usage = self.calculate_metrics(account, current_time)
        
        max_asset = None
        max_asset_exposure = 0.0
        if account.gross_exposure > 0:
            for asset, exp in account.asset_exposures.items():
                if exp > max_asset_exposure:
                    max_asset_exposure = exp
                    max_asset = asset
            max_concentration = max_asset_exposure / account.gross_exposure
        else:
            max_concentration = 0.0

        # --- Margin Violations --- [1]
        if margin_usage > 0.90:
            if self.margin_90_start is None: self.margin_90_start = current_time
            elapsed = (current_time - self.margin_90_start).total_seconds() / 60.0
            if elapsed >= 30.0 and "margin_90" not in self.deductions_applied:
                self.risk_discipline_score = max(0.0, self.risk_discipline_score - 20)
                self.deductions_applied.add("margin_90")
        else:
            self.margin_90_start = None
            self.deductions_applied.discard("margin_90")

        if margin_usage > 0.95:
            if self.margin_95_start is None: self.margin_95_start = current_time
            elapsed = (current_time - self.margin_95_start).total_seconds() / 60.0
            if elapsed >= 15.0 and "margin_95" not in self.deductions_applied:
                self.risk_discipline_score = max(0.0, self.risk_discipline_score - 30)
                self.deductions_applied.add("margin_95")
        else:
            self.margin_95_start = None
            self.deductions_applied.discard("margin_95")

        if margin_usage > 0.98:
            if self.margin_98_start is None: self.margin_98_start = current_time
            elapsed = (current_time - self.margin_98_start).total_seconds() / 60.0
            if elapsed >= 10.0 and "margin_98" not in self.deductions_applied:
                self.risk_discipline_score = max(0.0, self.risk_discipline_score - 50)
                self.deductions_applied.add("margin_98")
        else:
            self.margin_98_start = None
            self.deductions_applied.discard("margin_98")

        # --- Leverage Violations --- [1]
        if leverage > 28.0:
            if self.leverage_28_start is None: self.leverage_28_start = current_time
            elapsed = (current_time - self.leverage_28_start).total_seconds() / 60.0
            if elapsed >= 30.0 and "leverage_28" not in self.deductions_applied:
                self.risk_discipline_score = max(0.0, self.risk_discipline_score - 20)
                self.deductions_applied.add("leverage_28")
        else:
            self.leverage_28_start = None
            self.deductions_applied.discard("leverage_28")

        if leverage > 29.0:
            if self.leverage_29_start is None: self.leverage_29_start = current_time
            elapsed = (current_time - self.leverage_29_start).total_seconds() / 60.0
            if elapsed >= 15.0 and "leverage_29" not in self.deductions_applied:
                self.risk_discipline_score = max(0.0, self.risk_discipline_score - 30)
                self.deductions_applied.add("leverage_29")
        else:
            self.leverage_29_start = None
            self.deductions_applied.discard("leverage_29")

        # --- Concentration Violations --- [1]
        if max_concentration > 0.90 and leverage > 1.0:
            if self.concentration_90_start is None: self.concentration_90_start = current_time
            elapsed = (current_time - self.concentration_90_start).total_seconds() / 60.0
            if elapsed >= 30.0 and "concentration_90" not in self.deductions_applied:
                self.risk_discipline_score = max(0.0, self.risk_discipline_score - 10)
                self.deductions_applied.add("concentration_90")
        else:
            self.concentration_90_start = None
            self.deductions_applied.discard("concentration_90")

    def validate_trade(self, account: AccountState, asset: str, trade_size: float, current_time) -> bool:
        if not self.check_rate_limit():
            return False
            
        if current_time.hour == 21 and current_time.minute >= 50:
            return False
            
        if not self.is_session_liquid(asset, current_time):
            return False

        drawdown, leverage, margin_usage = self.calculate_metrics(account, current_time)
        if drawdown >= self.HARD_DRAWDOWN_LIMIT:
            return False

        asset_clean = asset.replace("/", "").replace("_", "")
        is_crypto = any(c in asset_clean for c in ["BTC", "ETH", "SOL", "XRP", "BAR"])
        is_metal = any(m in asset_clean for m in ["XAU", "XAG"])
        asset_class = "CRYPTO" if is_crypto else ("METALS" if is_metal else "FOREX")

        current_asset_exposure = account.asset_exposures.get(asset_clean, 0.0)
        projected_asset_exposure = current_asset_exposure + trade_size
        projected_gross_exposure = account.gross_exposure + trade_size
        
        if account.equity <= 0:
            return False
            
        projected_leverage = projected_gross_exposure / account.equity
        projected_concentration = projected_asset_exposure / projected_gross_exposure if projected_gross_exposure > 0 else 0.0
        
        required_margin_rate = self.margin_rates.get(asset_class, 0.0333)
        projected_used_margin = account.used_margin + (trade_size * required_margin_rate)
        projected_margin_usage = projected_used_margin / account.equity
        
        if projected_margin_usage > 0:
            projected_margin_level = account.equity / projected_used_margin
            if projected_margin_level <= 0.40:  
                return False

        limit = self.max_leverage_limits.get(asset_clean, self.max_leverage_limits["FOREX"] if asset_class == "FOREX" else 1.0)
        if projected_leverage > limit:
            return False

        if projected_leverage >= 29.5 or projected_margin_usage >= 0.97:
            return False

        return True

    def get_sharpe_ratio(self) -> float:
        return calculate_standalone_sharpe(self.equity_history_15m)