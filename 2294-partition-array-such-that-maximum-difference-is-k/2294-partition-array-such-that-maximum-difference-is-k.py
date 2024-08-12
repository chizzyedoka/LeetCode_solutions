class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = nums[0]
        res = 1
        for i in range(1, len(nums)):
            diff = nums[i] - start
            if diff > k:
                res += 1
                start = nums[i]
        return res