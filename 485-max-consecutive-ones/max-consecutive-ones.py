class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        seen_ones = 0
        max_ones = 0

        for num in nums:
            if num == 1:
                seen_ones += 1
                max_ones = max(seen_ones, max_ones)
            else:
                seen_ones = 0
        return max_ones