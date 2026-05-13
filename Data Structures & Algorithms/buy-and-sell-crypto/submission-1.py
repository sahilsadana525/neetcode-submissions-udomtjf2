from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: # Handle empty list case
            return 0
        
        min_price = float('inf') # Initialize min_price to a very large number
        max_profit = 0 # Initialize max_profit to 0
        
        for price in prices:
            if price < min_price:
                min_price = price # Update min_price if current price is lower
            elif price - min_price > max_profit:
                max_profit = price - min_price # Update max_profit if a better profit is found
                
        return max_profit