class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dfs(i):
            if i < 3:
                return i
            return dfs(i-2) + dfs(i-1)
        return dfs(n)