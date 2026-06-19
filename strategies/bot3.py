# strategies/bot3.py
import numpy as np

class Bot3:
    """
    Bot 3: Statistical Mean Reversion (Z-Score).
    Sells overbought extremes and buys oversold extremes.
    """
    def __init__(self, window: int = 30, z_threshold: float = 2.5):
        # Default optimized to 2.5 based on Fold 2 cross-validation
        self.window = window
        self.z_threshold = z_threshold

    def evaluate(self, mid_price: float, price_history: list) -> str:
        if len(price_history) < self.window:
            return "HOLD"
            
        window_prices = np.array(price_history[-self.window:])
        mean_val = np.mean(window_prices)
        std_val = np.std(window_prices)
        
        if std_val < 1e-8:
            return "HOLD"
            
        z_score = (mid_price - mean_val) / std_val
        
        if z_score < -self.z_threshold:
            return "BUY"
        elif z_score > self.z_threshold:
            return "SELL"
            
        return "HOLD"