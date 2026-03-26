class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size = float("inf")
        window_sum = 0
        start = 0

        for end in range(len(nums)):
            window_sum += nums[end]
            while window_sum >= target:
                window_size = end - start + 1
                min_size = min(min_size, window_size)
                window_sum -= nums[start]
                start += 1
    
        print(min_size)
        if min_size != float("inf"):
            return min_size 
        return 0
