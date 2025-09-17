class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        LAND = "1"
        WATER = "0"
        count = 0
        visited = set()
        
        def explore(r,c):
            if 0 <= r < m and 0 <= c < n and grid[r][c] == LAND and (r,c) not in visited:
                visited.add((r,c))
                explore(r+1, c)
                explore(r-1, c)
                explore(r, c+1)
                explore(r, c-1)
                return True
                
            else:
                return False



        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == LAND:
                    if explore(r,c):
                        count += 1
                    

        return count
