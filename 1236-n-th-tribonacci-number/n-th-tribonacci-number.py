class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return n
        if n <= 2:
            return 1

        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n+1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        return dp[n]

class Solution:
    def tribonacci(self, n: int) -> int:

        memo = {0: 0, 1: 1, 2: 1}

        def dp(i):
            if i not in memo:
                memo[i] = dp(i-3) + dp(i-2) + dp(i-1)
            return memo[i]

        return dp(n)