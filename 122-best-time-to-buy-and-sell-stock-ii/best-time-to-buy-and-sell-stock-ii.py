class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cp = prices[0]
        max_profit = 0
        for price in prices[1:]:
            profit = price - cp
            if profit > 0:
                max_profit += profit
            cp = price
        return max_profit