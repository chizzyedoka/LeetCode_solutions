class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        rows, cols = len(grid), len(grid[0])
        EMPTY = 0
        OBSTACLE = 1

        queue = deque([(0,0, k, 0)])
        visited = {(0,0, k)}
        destination = (rows-1, cols-1)
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        while queue:
            size = len(queue)
            for _ in range(size):
                r, c, k, distance = queue.popleft()
                if (r,c) == destination:
                    return distance
                for (dr, dc) in directions:
                    nr, nc = r+dr, c+dc
                    row_inbounds = 0<= nr < rows
                    col_inbounds = 0 <= nc < cols
    
                    if row_inbounds and col_inbounds:
                        if grid[nr][nc] == OBSTACLE: 
                            k_left = k - 1
                        else:
                            k_left = k
                            
                        if k_left >= 0 and (nr, nc, k_left) not in visited:
                            queue.append((nr,nc, k_left, distance+1))
                            visited.add((nr,nc, k_left))
            
        return -1
