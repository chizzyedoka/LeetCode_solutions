class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        count = 1
        for i in range(1,len(nums)-1):
            if nums[i] == nums[i-1]:
                count += 1
            if nums[i] != nums[i-1]:
                count = 1
            if nums[i] != nums[i+1] and count == 1:
                return nums[i]
        return nums[-1]