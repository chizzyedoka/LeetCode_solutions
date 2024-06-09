class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot(nums):
            left, right = 0, len(nums)-1
            while left < right:
                mid = (left+right)//2
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        def binary_search(nums, target, left, right):
            while left <= right:
                mid = (left + right)// 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return mid
            return -1
        
        pivot = find_pivot(nums) # smallest number in arr
        found_index = binary_search(nums, target, 0, pivot)
        if found_index == -1:
            found_index = binary_search(nums, target, pivot, len(nums)-1)
        return found_index
                
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums)-1
#         while left<=right:
#             mid = left+(right-left)//2
#             if nums[mid] == target:
#                 return mid
#             if nums[mid]<nums[right]:
#                 if nums[mid]<target<=nums[right]:
#                     left=mid+1
#                 else:
#                     right=mid-1
#             else:
#                 if nums[left]<=target<nums[mid]:
#                     right=mid-1
#                 else:
#                     left = mid+1
#         return -1