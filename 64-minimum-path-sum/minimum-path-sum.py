class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}
        def dp(i, j):
            if i < 0 or j < 0:
                return float(inf)
            
            if i ==0 and j ==0:
                return grid[i][j]
            if (i, j) not in memo:
                right_sum = dp(i,j-1)
                down_sum =  dp(i-1,j)
                min_sum = grid[i][j] + min(right_sum, down_sum)
                memo[(i,j)] = min_sum
            return memo[(i,j)]
        return dp(m-1, n-1)