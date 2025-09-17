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


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()
        q = deque()

        LAND = "1"
        directions = [(-1,0), (1,0), (0, -1), (0, 1)]
        count = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == LAND and (r,c) not in seen:
                    q.append((r,c))
                    while q:
                        i, j = q.popleft()
                        seen.add((i,j))
                        for (di, dj) in directions:
                            new_i, new_j = i + di, j + dj
                            if (0 <= new_i < m) and (0 <= new_j < n) and grid[new_i][new_j] == LAND and (new_i, new_j) not in seen:
                                q.append((new_i, new_j)) 
                                seen.add((new_i, new_j))
                    count += 1

        return count

