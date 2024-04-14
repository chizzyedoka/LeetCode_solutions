class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            index = nums[i]-1
            if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
            else:
                i += 1
                
        for index in range(len(nums)):
            if nums[index] != index+1:
                return index +1
        return len(nums)+1