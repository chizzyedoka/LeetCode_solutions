class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        # transpose
        for r in range(m):
            for c in range(r+1, m):
                matrix[c][r], matrix[r][c] = matrix[r][c], matrix[c][r]

        # reflect
        for r in range(m):
            for c in range((n+1)//2):
                matrix[r][c], matrix[r][-c-1] = matrix[r][-c-1], matrix[r][c]
        