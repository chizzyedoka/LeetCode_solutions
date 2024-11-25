class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def getPivot(nums): # smallest element in array
            l, r = 0, len(nums)-1
            while l < r:
                mid = (l + r) // 2
                if nums[mid] > nums[r]:
                     l = mid + 1
                else:
                    r = mid
            return r 
        
        def findTarget(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
                    
        pivotIndex = getPivot(nums)
        targetIndex = findTarget(0, pivotIndex)
        if targetIndex == -1:
            targetIndex = findTarget(pivotIndex, len(nums)-1)
        return targetIndex