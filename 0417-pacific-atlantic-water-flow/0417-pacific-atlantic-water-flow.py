class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_q = deque()
        pacific_seen = set()
        
        atlantic_q = deque()
        atlantic_seen = set()
        
        rows, cols = len(heights), len(heights[0])
        
        for j in range(cols):
            pacific_q.append((0,j))
            pacific_seen.add((0,j))
            
        for i in range(1,rows):
            pacific_q.append((i,0))
            pacific_seen.add((i,0))
            
        for i in range(rows):
            atlantic_q.append((i,cols-1))
            atlantic_seen.add((i, cols-1))
            
        for j in range(cols-1):
            atlantic_q.append((rows-1,j))
            atlantic_seen.add((rows-1,j))
            
        def get_coords(q,seen):
            while q:
                (i,j) = q.popleft()
                for (i_off,j_off) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    r,c = i+i_off, j+j_off
                    row_inbounds = 0 <= r < rows
                    col_inbounds = 0 <= c < cols
                    if row_inbounds and col_inbounds and heights[r][c] >= heights[i][j] and (r,c) not in seen:
                        q.append((r,c))
                        seen.add((r,c))
        
        get_coords(pacific_q, pacific_seen)
        get_coords(atlantic_q, atlantic_seen)
        return list(pacific_seen.intersection(atlantic_seen))
        
        
        
            