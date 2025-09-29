class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zeros = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros.add((i,j))

        
        if len(zeros) > 0:
            q = deque()
            for (zi, zj) in zeros:
                q.append((zi, zj))
            while q:
                i,j = q.popleft()
                # make rows zeros
                for r in range(m):
                    if r != i and (r,j) not in zeros:
                        matrix[r][j] = 0
                        zeros.add((r,j))
                # make cols zeros
                for c in range(n): 
                    if c != j and (i,c) not in zeros:
                        matrix[i][c] = 0
                        zeros.add((i,c))


        