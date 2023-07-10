class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        cur_sum = 0
        min_length = float('inf') 
        for right in range(len(nums)):
            cur_sum += nums[right]
            
            while cur_sum >= target:
                min_length = min(min_length, right-left+1)
                cur_sum -= nums[left]
                left += 1
        if min_length == float('inf'):
            return 0
        return(min_length)
                
        