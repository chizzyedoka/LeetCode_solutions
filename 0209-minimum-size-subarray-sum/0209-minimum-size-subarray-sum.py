class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float('inf')
        start = 0
        window_sum = 0
        for end in range(len(nums)):
            window_sum += nums[end]
            while window_sum >= target:
                window = nums[start:end+1]
                window_size = len(window)
                minLength = min(minLength,window_size)
                window_sum -= nums[start]
                start += 1
        if minLength == float('inf'):
            return 0
        return minLength 
                
            
            
        