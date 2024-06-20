class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, cols-1
        while r < rows and c>=0:
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]>target:
                c-=1 # move left
            else:
                r+= 1 # move down
        return None