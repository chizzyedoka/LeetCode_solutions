class Solution:
    def myPow(self, x: float, n: int) -> float:
        memo = {}
        def helper(x, n):
            if n == 0:
                return 1
            elif n == 1:
                return x
            if n in memo:
                return memo[n]
            if n% 2 == 0:
                memo[n] = helper(x, n//2) * helper(x, n//2)
            elif n % 2 != 0:
                memo[n] = x * helper(x, n//2) * helper(x, n//2)
            return memo[n]
        is_neg = n < 0
        n = abs(n)
        if is_neg:
            return 1/helper(x, n)
        return helper(x, n)