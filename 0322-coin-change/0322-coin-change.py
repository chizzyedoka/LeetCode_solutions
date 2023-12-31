# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int: 
#         count = 0
#         coins.sort(reverse=True)
#         while amount > 0 and amount > min(coins):
#             for coin in coins:
#                 if amount >= coin:
#                     q = amount // coin
#                     count += q
#                     amount = amount % coin
#         if amount != 0 and amount < min(coins):
#                 return -1
#         elif amount != 0 and amount == min(coins) and len(coins)==1:
#             return 1
#         return count
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize an array to store the minimum number of coins needed for each amount
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Zero coins needed to make change for amount 0

        # Iterate through each coin and update the dp array
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        # If dp[amount] is still float('inf'), no valid combination was found
        return dp[amount] if dp[amount] != float('inf') else -1

            
                