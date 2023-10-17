class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums)%2 != 0:
            return float(nums[(len(nums)//2)])
        first = nums[int((len(nums)/2)-1)]
        second = nums[len(nums)//2]
        return float(first+second)/2
