class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}
        def dp(m,n):
            if m==1 and n==1:
                return 1
            elif m ==1:
                return 1
            elif n==1:
                return 1
            if (m,n) not in memo:
                right = dp(m,n-1)
                down = dp(m-1, n)
                memo[(m,n)] =  right + down
            return memo[(m,n)]
        
        return dp(m,n)