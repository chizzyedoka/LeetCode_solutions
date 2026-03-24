class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [-1] * n

        if k == 0:
            return nums

        if k > n:
            return result
       
        window_size = (2*k + 1)
        window_sum = sum(nums[:window_size])
        result[k] = window_sum// window_size
        
        for end in range(k+1, n-k):
            start_index = end - k - 1
            stop_index =  end + k
            window_sum = window_sum - nums[start_index] + nums[stop_index]
            avg = window_sum // window_size
            result[end] = avg
        return result


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [-1] * n
        
        if k == 0:
            return nums
        
        window_size = 2 * k + 1
        
        if window_size > n:
            return result
        
        window_sum = sum(nums[:window_size])
        result[k] = window_sum // window_size
        
        for end in range(k + 1, n - k):
            window_sum = window_sum - nums[end - k - 1] + nums[end + k]
            result[end] = window_sum // window_size
        
        return result
