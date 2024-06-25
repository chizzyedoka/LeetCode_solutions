class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # go through the matrix, count how many fresh oranges, rotten oranges we have
        # create a counter for minutes spents for each iteration
        # at the end of iteration check if the amount of freshoranges is zero
        
        q = deque()
        empty, fresh, rotten = 0, 1, 2
        minutes = -1
        freshOranges = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == fresh:
                    freshOranges += 1
                elif grid[r][c] == rotten:
                    q.append((r,c))
        if freshOranges == 0:
            return 0
        
        while q:
            minutes += 1
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                for (r,c) in [(i+1,j), (i-1,j), (i, j-1), (i, j+1)]:
                    row_inbounds = 0 <= r < len(grid)
                    col_inbounds = 0 <= c < len(grid[0])
                    if row_inbounds and col_inbounds and grid[r][c] == fresh:
                        grid[r][c] = rotten
                        freshOranges -= 1
                        q.append((r,c))
                    
        if freshOranges == 0:
            return minutes
        else:
            return -1