class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        seen_zeros = 0
        max_ones = 0
        start = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                seen_zeros += 1

            while seen_zeros > k:
                if nums[start] == 0:
                    seen_zeros -= 1
                start += 1
                
            window = end - start + 1
            max_ones = max(window, max_ones)
        return max_ones