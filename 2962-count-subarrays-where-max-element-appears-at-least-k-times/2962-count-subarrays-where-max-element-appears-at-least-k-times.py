class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        max_count = 0
        res=window_start=0
        for window_end in range(len(nums)):
            if nums[window_end] == max_element:
                max_count += 1
                
            while max_count >= k:
                if nums[window_start] == max_element:
                    max_count -= 1
                window_start += 1
            res += window_start
        return res
    
# class Solution:
#     def countSubarrays(self, nums: List[int], k: int) -> int:
#         max_el = max(nums)
#         res = 0
#         window_start = 0
#         seen_max = 0
        
#         for window_end in range(len(nums)):
#             if nums[window_end] == max_el:
#                 seen_max += 1
            
#             while seen_max >= k:
#                 if nums[window_start] == max_el:
#                     seen_max -= 1
#                 window_start += 1
            
#             res += window_start
        
#         return res



            
        