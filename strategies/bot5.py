# strategies/bot5.py

class Bot5:
    """
    Bot 5: Lead-Lag Cross-Asset Correlation.
    Identifies momentum shifts in leading assets to predict lagging targets.
    """
    def __init__(self, threshold_pct: float = 0.0005):
        self.threshold_pct = threshold_pct
        # Correlation mapping: {lagging_asset: leading_asset}
        self.lead_lag_map = {
            "GBPUSD": "EURUSD",
            "XAGUSD": "XAUUSD",
            "ETHUSD": "BTCUSD",
            "SOLUSD": "BTCUSD",
            "XRPUSD": "BTCUSD"
        }

    def evaluate(self, symbol: str, current_prices: dict, price_histories: dict) -> str:
        leader = self.lead_lag_map.get(symbol)
        if not leader:
            return "HOLD"
            
        leader_history = price_histories.get(leader, [])
        if len(leader_history) < 2:
            return "HOLD"
            
        # Compare the last two recorded mid prices
        leader_prev = leader_history[-2]
        leader_curr = leader_history[-1]
        
        if leader_prev <= 0:
            return "HOLD"
            
        leader_return = (leader_curr - leader_prev) / leader_prev
        
        if leader_return > self.threshold_pct:
            return "BUY"
        elif leader_return < -self.threshold_pct:
            return "SELL"
            
        return "HOLD"