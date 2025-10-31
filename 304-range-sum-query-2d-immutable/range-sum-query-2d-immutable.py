class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefix = [[0]*COLS for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                top = self.prefix[r-1][c]  if (r-1) >= 0 else 0
                left = self.prefix[r][c-1] if (c-1) >= 0 else 0
                topLeft = self.prefix[r-1][c-1] if (r-1) >= 0 and (c-1) >= 0  else 0
                self.prefix[r][c] = matrix[r][c] + top + left - topLeft

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix[row2][col2]
        top = self.prefix[row1-1][col2] if row1 > 0 else 0
        left = self.prefix[row2][col1-1] if col1 > 0 else 0
        topLeft = self.prefix[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
        return total - top - left + topLeft

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)