class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_index = 0
        maxProfit = float('-inf')
        for i in range(len(prices)):
            if prices[i] < prices[buy_index]:
                buy_index = i
            elif prices[i] - prices[buy_index] > maxProfit:
                maxProfit = prices[i] - prices[buy_index]
        return maxProfit
#         i = 1
#         buy_index = 0
#         sell_index = len(prices)-1
#         j = len(prices) - 2
#         while buy_index < sell_index:
#             if prices[i] < prices[buy_index]:
#                 buy_index=i
#             if prices[j] > prices[sell_index]:
#                 sell_index=j
#             i += 1
#             j-=1
#         maxProfit = prices[sell_index]- prices[buy_index]
#         if maxProfit > 0:
#             return maxProfit
#         return 0
            
        