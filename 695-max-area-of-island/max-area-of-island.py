class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        LAND = 1
        self.max_area = 0
        self.area = 0
        visited = set()

        def dfs(r,c):
            row_inbounds = 0 <= r < rows
            col_inbounds = 0 <= c < cols

            if row_inbounds and col_inbounds and grid[r][c] == LAND and (r,c) not in visited:
                visited.add((r,c))
                self.area += 1
                dfs(r+1,c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)
            else:
                return

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == LAND and (i,j) not in visited:
                    self.area = 0
                    dfs(i,j)
                    self.max_area = max(self.max_area, self.area)

        return self.max_area

