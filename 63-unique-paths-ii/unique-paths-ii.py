class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = {}
        
        def dfs(i,j):

            row_inbounds = 0 <= i < m
            col_inbounds = 0 <= j < n 

            if not row_inbounds or not col_inbounds or obstacleGrid[i][j] == 1:
                memo[(i,j)] = 0
                return 0

            if (i,j) == (m-1,n-1):
                memo[(i,j)] = 1
                return 1

            if (i,j) in memo:
                return memo[(i,j)]


            down = dfs(i+1,j)
            right = dfs(i, j+1)

            memo[(i,j)] = right + down
            return memo[(i,j)]

        return dfs(0,0)