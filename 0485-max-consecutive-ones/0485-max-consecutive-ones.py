class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count_ones = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count_ones += 1
                res = max(count_ones,res)
            else:
                count_ones = 0
        return res