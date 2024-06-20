class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rows, cols = len(matrix), len(matrix[0])
        left , right = 0, (rows * cols) - 1
        
        while left <= right:
            mid = (left+right)//2
            mid_value = matrix[mid // cols][mid%cols]
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         rows, cols = len(matrix), len(matrix[0])
#         r, c = 0, cols-1
#         while r < rows and c>=0:
#             if matrix[r][c]==target:
#                 return True
#             elif matrix[r][c]>target:
#                 c-=1 # move left
#             else:
#                 r+= 1 # move down
#         return None