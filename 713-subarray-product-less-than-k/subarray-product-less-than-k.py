class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        result = 0
        start = 0
        window_product = 1

        for end in range(len(nums)):
            window_product *= nums[end]
            
            while window_product >= k:
                window_product /= nums[start]
                start += 1
            result += end - start + 1

        return result