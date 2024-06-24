class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        row, column = len(grid), len(grid[0])
        for r in range(row):
            for c in range(column):
                if grid[r][c] == '1' and (r,c) not in visited:
                    count += 1
                    self.explore(grid, r, c, visited)
        return count

    def explore(self,grid, r, c, visited):
        row_inbounds = 0 <= r < len(grid)
        col_inbounds = 0 <= c < len(grid[0])
        if not row_inbounds or not col_inbounds:
            return False

        if grid[r][c] == '0':
            return False

        pos = (r,c)
        if pos in visited:
            return False
        visited.add(pos)

        self.explore(grid, r-1, c, visited)
        self.explore(grid, r+1, c, visited)
        self.explore(grid, r, c-1, visited)
        self.explore(grid, r, c+1, visited)
        