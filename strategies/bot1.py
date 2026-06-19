# strategies/bot1.py

class Bot1:
    """
    Bot 1: Order Book Imbalance (OBI).
    Detects structural supply and demand imbalances in the order book depth.
    """
    def __init__(self, threshold: float = 0.45):
        # Default optimized to 0.45 based on Fold 2 cross-validation
        self.threshold = threshold

    def evaluate(self, row) -> str:
        # Fast path: Use pre-calculated column
        if 'book_imbalance' in row:
            try:
                imbalance = float(row['book_imbalance'])
                if imbalance > self.threshold:
                    return "BUY"
                elif imbalance < -self.threshold:
                    return "SELL"
            except (ValueError, TypeError):
                pass
        
        # Fallback path: Calculate directly from raw lists if present
        try:
            total_bids = sum(row.get('bidsizes', []))
            total_asks = sum(row.get('asksizes', []))
            if (total_bids + total_asks) > 0:
                imbalance = (total_bids - total_asks) / (total_bids + total_asks)
                if imbalance > self.threshold:
                    return "BUY"
                elif imbalance < -self.threshold:
                    return "SELL"
        except Exception:
            pass
            
        return "HOLD"