class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        if n == 2:
            return min(cost[0], cost[1])

        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[n]

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        if n == 2:
            return min(cost[0], cost[1])

        memo = {}

        def dp(i):
            if i < 2:
                return 0
            if i not in memo:
                memo[i] =  min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])
            return memo[i]

        return dp(n)