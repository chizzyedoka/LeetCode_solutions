class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(curAmount):
            if curAmount == 0:
                return 0
            if curAmount < 0:
                return -1

            minCoins = float('inf')
            if curAmount not in memo:
                for coin in coins:
                    res = dfs(curAmount - coin)
                    if res != -1:
                        minCoins = min(minCoins, 1+res)
                memo[curAmount] = minCoins if minCoins != float('inf') else -1
            return memo[curAmount]
            
        return dfs(amount)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        coins.sort()

        for i in range(1, amount+1):
            minCoins = float('inf')
            for coin in coins:
                diff = i - coin
                if diff < 0:
                    break
                minCoins = min(minCoins, 1+dp[diff])
            dp[i] = minCoins 
        return dp[-1] if dp[-1] != float('inf') else -1
