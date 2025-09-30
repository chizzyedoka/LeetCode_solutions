class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def getPivot(nums):
            left, right = 0, len(nums) -1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            return left - 1

        def binarySearch(left, right):
            while left <= right:
                mid = (left+right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        pivot = getPivot(nums)
        position = binarySearch(0,pivot)
        # check first half
        if position != -1:
            return position
        return binarySearch(pivot+1, len(nums)-1)


                