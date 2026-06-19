# alpha_agent.py
import sys
import os

# Ensure Python looks in the current directory for the strategies package
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from strategies.bot1 import Bot1
from strategies.bot2 import Bot2
from strategies.bot3 import Bot3
from strategies.bot4 import Bot4
from strategies.bot5 import Bot5

class FiveBotAlphaCouncil:
    def __init__(self):
        self.price_histories = {} # {symbol: [list of historical prices]}
        self.bot1 = Bot1()
        self.bot2 = Bot2()
        self.bot3 = Bot3()
        self.bot4 = Bot4()
        self.bot5 = Bot5()

    def update_price(self, symbol: str, mid_price: float):
        """Maintains price history records sequentially."""
        if symbol not in self.price_histories:
            self.price_histories[symbol] = []
        self.price_histories[symbol].append(mid_price)
        
        # Limit history length to 100 to prevent memory leaks [1]
        if len(self.price_histories[symbol]) > 100:
            self.price_histories[symbol].pop(0)

    def evaluate_market(self, row, symbol: str) -> dict:
        mid_price = (float(row['bid']) + float(row['ask'])) / 2.0
        history = self.price_histories.get(symbol, [])
        
        # Gather votes from individual bot classes
        v1 = self.bot1.evaluate(row)
        v2 = self.bot2.evaluate(history)
        v3 = self.bot3.evaluate(mid_price, history)
        v4 = self.bot4.evaluate(history)
        
        # Compile latest mid prices for the lead-lag calculations [1]
        current_prices = {}
        for sym, hist in self.price_histories.items():
            if hist:
                current_prices[sym] = hist[-1]
                
        v5 = self.bot5.evaluate(symbol, current_prices, self.price_histories)
        
        votes = {"Bot1": v1, "Bot2": v2, "Bot3": v3, "Bot4": v4, "Bot5": v5}
        vote_values = list(votes.values())
        buy_count = vote_values.count("BUY")
        sell_count = vote_values.count("SELL")
        
        final_signal = "HOLD"
        vote_strength = 0
        
        # Consensus gate: requires a majority of 3+ agreement [1]
        if buy_count >= 3 and buy_count > sell_count:
            final_signal = "BUY"
            vote_strength = buy_count
        elif sell_count >= 3 and sell_count > buy_count:
            final_signal = "SELL"
            vote_strength = sell_count
            
        return {
            "signal": final_signal,
            "vote_strength": vote_strength,
            "votes": votes
        }