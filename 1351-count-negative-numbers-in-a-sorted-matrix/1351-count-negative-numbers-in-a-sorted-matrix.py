class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        def binary_search(row):
            left, right =  0, len(row)-1
            while left <= right:
                mid = (left+right)//2
                if row[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
            return len(row)-left
        for row in grid:
            count += binary_search(row)
        return count
                    