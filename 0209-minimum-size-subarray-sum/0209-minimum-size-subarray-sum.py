class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float('inf')
        start = 0
        window_sum = 0
        for end in range(len(nums)):
            window_sum += nums[end]
            while window_sum >= target:
                minLength = min(minLength, end-start+1)
                window_sum -= nums[start]
                start += 1
        if minLength == float('inf'):
            return 0
        return minLength 
       
                
            
            
        