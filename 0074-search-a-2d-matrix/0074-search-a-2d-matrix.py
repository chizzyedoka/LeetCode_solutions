class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        
        # [1,3,5,7,10,11,16,20,23,30,34,60]
        l,r = 0, m*n-1
        while l <= r:
            mid = (l+r)//2
            i, j = mid// n, mid%n
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                r = mid -1
            else:
                l = mid + 1
        return False
            
        