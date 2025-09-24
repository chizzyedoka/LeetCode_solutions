class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        possible_exit = set()
        for c in range(n):
            possible_exit.add((0, c))
            possible_exit.add((m-1, c))

        for r in range(m):
            possible_exit.add((r,0))
            possible_exit.add((r,n-1))

        if (entrance[0], entrance[1]) in possible_exit:
            possible_exit.remove((entrance[0], entrance[1]))
        
        WALL = "+"
        FREE = "."
        steps = 0
        exits = possible_exit
        visited = set()
        for r in range(m):
            for c in range(n):
                if maze[r][c] == WALL and (r,c) in possible_exit:
                    possible_exit.remove((r,c))

        q = deque([entrance])
        directions = [(0,-1), (0,1), (-1,0), (1,0)]
        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                if (i,j) in exits:
                    return steps
                for (di, dj) in directions:
                    r,c = i+di, j+dj
                    if 0 <= r < m and 0 <= c < n and maze[r][c] == FREE and (r,c) not in visited:
                        q.append((r,c))
                        visited.add((r,c))
            steps += 1

        return -1
