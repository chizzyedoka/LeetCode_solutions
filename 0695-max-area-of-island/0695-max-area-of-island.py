class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def explore(grid, r, c, visited):
            row_inbounds = 0 <= r < len(grid)
            col_inbounds = 0 <= c < len(grid[0])
            if not row_inbounds or not col_inbounds:
                return 0
            pos = (r,c)
            if pos in visited or grid[r][c]==0:
                return 0
            visited.add(pos)
            
            area = 1
            area += explore(grid, r+1, c, visited)
            area += explore(grid, r-1, c, visited)
            area += explore(grid, r, c+1, visited)
            area += explore(grid, r, c-1, visited)
            return area
                
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                area = explore(grid, r, c, visited)
                max_area = max(max_area, area)
        return max_area