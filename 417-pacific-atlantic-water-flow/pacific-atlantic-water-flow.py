class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific_q = deque()
        atlantic_q = deque()

        pacific_seen = set()
        atlantic_seen = set()

        # fill pacific queue -> first column
        for r in range(m):
            pacific_q.append((r,0))
            pacific_seen.add((r,0))

        # fill pacific queue -> first row
        for c in range(n):
            pacific_q.append((0, c))
            pacific_seen.add((0,c))

        # fill atlantic queue -> last row
        for c in range(n) :
            atlantic_q.append((m-1, c))
            atlantic_seen.add((m-1, c))

        # fill atlantic queue -> last col
        for r in range(m) :
            atlantic_q.append((r, n-1))
            atlantic_seen.add((r, n-1))

        def getCord(q, visited):
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            while q:
                i,j = q.popleft()
                for dr, dc in directions:
                    r, c = i+dr, j+dc
                    if 0 <= r < m and 0 <= c < n and heights[r][c] >= heights[i][j]:
                        if (r,c) not in visited:
                            visited.add((r,c))
                            q.append((r,c))

        getCord(pacific_q, pacific_seen)
        getCord(atlantic_q, atlantic_seen)
        return list(pacific_seen.intersection(atlantic_seen))