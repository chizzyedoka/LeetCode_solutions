class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        hashmap={0:0}
        window_start, max_length = 0, 0
        for window_end in range(len(nums)):
            if nums[window_end] == 0:
                hashmap[0] += 1
            while hashmap[0] > 1:
                if nums[window_start] == 0:
                    hashmap[0] -= 1
                window_start += 1
            max_length = max(max_length, window_end-window_start)
        return max_length
    
