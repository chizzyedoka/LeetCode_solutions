class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        while i < len(nums):
            correct_index = nums[i]-1
            if nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if i+1 != nums[i]:
                res.append(nums[i])
        return res