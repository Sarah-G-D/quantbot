# strategies/bot2.py
import numpy as np

class Bot2:
    """
    Bot 2: Volatility-Filtered EMA Momentum.
    EMA crossovers are executed only when volatility is expanding.
    """
    def __init__(self, fast: int = 5, slow: int = 15, vol_window: int = 20):
        self.fast = fast
        self.slow = slow
        self.vol_window = vol_window

    def evaluate(self, price_history: list) -> str:
        if len(price_history) < self.vol_window:
            return "HOLD"
        
        # Convert only the slice we need to a numpy array to save CPU cycles
        prices = np.array(price_history[-self.vol_window:])
        
        fast_ma = np.mean(prices[-self.fast:])
        slow_ma = np.mean(prices[-self.slow:])
        
        recent_std = np.std(prices)
        
        # Safe lookup for previous standard deviation
        if len(price_history) > self.vol_window:
            prev_prices = np.array(price_history[-self.vol_window-1:-1])
            prev_std = np.std(prev_prices)
        else:
            prev_std = recent_std
        
        # Only signal a trade if standard deviation is expanding
        if recent_std > prev_std:
            if fast_ma > slow_ma:
                return "BUY"
            elif fast_ma < slow_ma:
                return "SELL"
                
        return "HOLD"