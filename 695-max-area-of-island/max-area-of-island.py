class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area = 0
        max_area = 0
        LAND, WATER = 1, 0
        visited = set()

        def dfs(r,c):
            rowInbounds = 0 <= r < rows
            colInbounds = 0 <= c < cols
            if not rowInbounds or not colInbounds or (r,c) in visited or grid[r][c] == WATER:
                return 0

            visited.add((r,c))
            area = 1 +  (dfs(r+1,c) +
                    dfs(r-1,c) +
                    dfs(r,c+1) +
                    dfs(r,c-1))
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == LAND:
                    area = dfs(r,c)
                    max_area = max(area, max_area)
                   

        return max_area