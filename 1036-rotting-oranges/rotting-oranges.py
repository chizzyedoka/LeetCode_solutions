class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY,FRESH, ROTTEN = 0, 1, 2
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        mins = 0

        # get the number of rotten oranges and put them in a queue
        rotten_oranges_queue = deque()
        count_of_fresh_oranges = 0
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == FRESH:
                    count_of_fresh_oranges += 1
                elif grid[r][c] == ROTTEN:
                    rotten_oranges_queue.append((r,c))
                    

        if count_of_fresh_oranges == 0:
            return 0

        while rotten_oranges_queue and count_of_fresh_oranges > 0:
            size = len(rotten_oranges_queue)
            for _ in range(size):
                i,j = rotten_oranges_queue.popleft()
                for di,dj in directions:
                    ni, nj = i+di, j+dj
                    if (0 <= ni < rows) and (0 <= nj < cols) and grid[ni][nj] == FRESH:
                        grid[ni][nj] = ROTTEN
                        count_of_fresh_oranges -= 1
                        rotten_oranges_queue.append((ni,nj))
            mins += 1
                    
        if count_of_fresh_oranges == 0:
            return mins
       
        return -1




