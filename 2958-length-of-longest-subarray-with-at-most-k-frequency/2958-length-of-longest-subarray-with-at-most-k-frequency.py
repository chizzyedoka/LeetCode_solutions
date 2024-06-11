class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        nums_count = {}
        res = window_start = 0
        for window_end in range(len(nums)):
            num = nums[window_end]
            if num not in nums_count:
                nums_count[num] = 0
            nums_count[num] += 1
            
            while nums_count[num] > k:
                nums_count[nums[window_start]] -= 1
                if nums_count[nums[window_start]] == 0:
                    del nums_count[nums[window_start]]
                window_start += 1
            res = max(res,window_end - window_start + 1)
        return res