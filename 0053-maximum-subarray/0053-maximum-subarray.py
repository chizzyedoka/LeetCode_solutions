class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum, max_sum = 0, nums[0]
        for i in range(len(nums)):
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += nums[i]
            max_sum = max(cur_sum, max_sum)
        return max_sum