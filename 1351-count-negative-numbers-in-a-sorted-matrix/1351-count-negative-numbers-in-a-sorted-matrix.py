class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] < 0:
                    count += 1
        return count