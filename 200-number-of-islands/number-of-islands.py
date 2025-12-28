class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        LAND = "1"
        islands = 0
        visited = set()
        directions = [(-1,0), (1,0), (0,1), (0,-1)]

        def bfs(r,c):
            queue = deque()

            queue.append((r,c))
            visited.add((r,c))
            
            while queue:
                i, j = queue.popleft()
                for di,dj in directions:
                    new_i, new_j = i+di, j+dj
                    row_inbounds = 0 <= new_i < rows
                    col_inbounds = 0 <= new_j < cols
                    if row_inbounds and col_inbounds and grid[new_i][new_j]== LAND and (new_i, new_j) not in visited:
                        queue.append((new_i, new_j))
                        visited.add((new_i, new_j))
            





        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == LAND and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1

        return islands