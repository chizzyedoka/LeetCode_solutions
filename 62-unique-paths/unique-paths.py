class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dp(i,j):
            # base case
            if i <= 0 or j <= 0:
                return 0
            if i==1 and j == 1:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            
            memo[(i,j)] = dp(i-1, j) + dp(i, j-1)
            return memo[(i,j)]
            
        return dp(m,n)