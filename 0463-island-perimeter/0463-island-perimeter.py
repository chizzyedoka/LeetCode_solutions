class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        row, col = len(grid), len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return self.explore(grid, r, c, visited)
        return 0
                
    def explore(self, grid, r, c, visited):
        row_inbounds = 0 <= r < len(grid)
        col_inbounds = 0 <= c < len(grid[0])
        
        if not row_inbounds or not col_inbounds:
            return 1
        
        if grid[r][c] == 0:
            return 1
        
        pos = (r,c)
        if pos in visited:
            return 0
        visited.add(pos)
        perim = 0
        perim += self.explore(grid, r+1, c, visited)
        perim += self.explore(grid, r-1, c, visited)
        perim += self.explore(grid, r, c+1, visited)
        perim += self.explore(grid, r, c-1, visited)
        return perim
        