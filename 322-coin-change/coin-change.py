class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        # state dp
        def dp(remAmount): 
            # base case
            if remAmount < 0:
                return float('inf')
            if remAmount == 0:
                return 0

            # recursive solution
            min_coins = float("inf")

            if remAmount in memo:
                    return memo[remAmount]

            for coin in coins:
                res = dp(remAmount - coin)
                if res != float('inf'):
                    min_coins = min(min_coins, 1 + res)
            memo[remAmount] = min_coins
            
            return min_coins

        result = dp(amount)
        return result if result != float("inf") else -1

             