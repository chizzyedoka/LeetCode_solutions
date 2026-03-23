class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        result = window_sum / k
        start = 0
        
        for end in range(k, len(nums)):
            window_sum = window_sum + nums[end] - nums[start]
            start += 1
            result = max(result, window_sum/k)

        return result
        