class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count = 0
        result = 0
        start = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                zero_count += 1
            
            while zero_count > 1:
                if nums[start] == 0:
                    zero_count -= 1
                start += 1

            window = end - start 
            result = max(window, result)
        return result