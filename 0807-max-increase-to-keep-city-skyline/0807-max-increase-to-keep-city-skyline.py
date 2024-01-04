class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        hSkyline = []
        vSkyline = []
        total = 0
        originalTotal = 0
        for r in range(n):
            maxv = grid[0][r]
            maxh = 0
            for c in range(n):
                maxv = max(maxv, grid[c][r])
                maxh = max(maxh,grid[r][c])
                originalTotal += grid[r][c]
            vSkyline.append(maxv)
            hSkyline.append(maxh)
        for r in hSkyline:
            for c in vSkyline:
                total += min(r,c)
        return total - originalTotal
        