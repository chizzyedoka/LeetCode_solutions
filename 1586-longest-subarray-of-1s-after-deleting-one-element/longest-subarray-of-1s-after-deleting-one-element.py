class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        nums_count = {1:0, 0:0}
        result = 0
        start = 0

        for end in range(len(nums)):
            nums_count[nums[end]] += 1
            while nums_count[0] > 1:
                if nums[start] == 0:
                    nums_count[0] -= 1
                start += 1

            window = end - start 
            result = max(window, result)
        return result