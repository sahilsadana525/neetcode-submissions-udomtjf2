from typing import List 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                m = prices[j] - prices[i]
                if max < m:
                    max = m
        return max
