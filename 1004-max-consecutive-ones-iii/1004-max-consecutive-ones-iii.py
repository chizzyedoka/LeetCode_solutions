class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        seen_freq = {0:0}
        max_count, window_start= 0,0
        for window_end in range(len(nums)):
            if nums[window_end] ==0:
                seen_freq[0] += 1
            while seen_freq[0] > k:
                if nums[window_start] == 0:
                    seen_freq[0] -= 1
                window_start += 1
            max_count = max(max_count, window_end-window_start+1)
        return max_count


