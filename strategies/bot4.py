# strategies/bot4.py
import numpy as np

class Bot4:
    """
    Bot 4: Medium-Term Structural Trend Follower.
    Keeps the council aligned with the broader market direction.
    """
    def __init__(self, fast: int = 10, slow: int = 30):
        self.fast = fast
        self.slow = slow

    def evaluate(self, price_history: list) -> str:
        if len(price_history) < self.slow:
            return "HOLD"
            
        prices = np.array(price_history[-self.slow:])
        fast_ma = np.mean(prices[-self.fast:])
        slow_ma = np.mean(prices)
        
        if fast_ma > slow_ma:
            return "BUY"
        elif fast_ma < slow_ma:
            return "SELL"
            
        return "HOLD"