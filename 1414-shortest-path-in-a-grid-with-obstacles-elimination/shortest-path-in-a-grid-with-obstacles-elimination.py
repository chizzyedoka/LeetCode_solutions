class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        OBSTACLE = 1
        directions = [(0, 1), (0,-1), (1,0), (-1, 0)]
        # (row, col, remaining_k)
        q = deque()
        q.append((0,0,k,0))
        visited = set((0,0,k))

        while q:
            (r, c, rem, steps) = q.popleft()

            # reached destination
            if (r,c) == (m-1, n-1):
                return steps

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] == OBSTACLE:
                        new_rem = rem - 1
                    else: new_rem = rem
                    if new_rem >= 0 and (nr,nc, new_rem) not in visited:
                        visited.add((nr,nc, new_rem))
                        q.append((nr,nc, new_rem, steps+1))
        return -1