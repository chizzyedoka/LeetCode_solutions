class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        if grid[0][0] != 0:
            return -1
        if grid[m-1][n-1] != 0:
            return -1
        
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        visited = set()
        distance = 1
        queue = deque([(0,0)])

        while queue:
            size = len(queue)

            for _ in range(size):
                i, j = queue.popleft()
                if (i,j) == (m-1, n-1) and grid[i][j] == 0:
                    return distance 
                for (di, dj) in directions:
                    row_inbounds = 0 <= i + di < m
                    col_inbounds = 0<= j + dj < n
                    if row_inbounds and col_inbounds and grid[i+di][j+dj] == 0 and (i+di, j+dj) not in visited:
                        queue.append((i+di, j+dj))
                        visited.add((i+di, j+dj))
            distance += 1
        return -1
