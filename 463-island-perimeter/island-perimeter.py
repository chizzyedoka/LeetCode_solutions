class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        LAND = 1
        self.perimeter = 0
        visited = set()

        def dfs(r, c):
            row_inbounds = 0 <= r < rows
            col_inbounds = 0 <= c < cols

            # 1. Out of bounds or water counts as a perimeter boundary (+1)
            if not (row_inbounds and col_inbounds) or grid[r][c] != LAND:
                self.perimeter += 1
                return

            # 2. Already visited land has already been explored (no new boundary)
            if (r, c) in visited:
                return

            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == LAND:
                    dfs(i, j)
                    return self.perimeter  # Return immediately since there is at most one island

        return 0