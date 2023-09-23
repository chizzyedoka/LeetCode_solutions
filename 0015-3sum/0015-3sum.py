class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array
        nums.sort()
        triplets = []
        # loop through the array and for each iteration find two other elements with a sum of arr[i]
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == -nums[i]:
                    ans = [nums[i],nums[left],nums[right]]
                    if ans not in triplets:
                        triplets.append(ans)
                    left += 1
                    right -=1
                elif -nums[i] > current_sum:
                    left += 1
                else:
                    right -= 1
        return triplets
    
#     class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         # [-1,0,1,2,-1,-4] --> [-4, -1, -1, 0 , 1, 2]
#         # i = 0

#                     # k = 1
        
#         result = []
#         nums.sort()
        
        
#         for i in range(len(nums)):
#             j = len(nums) - 1
#             k = i + 1
#             while k < j:
#                 sum_ = nums[i] + nums[j] + nums[k]
#                 if sum_ == 0: 
#                     ans = [nums[i], nums[j], nums[k]]
#                     if ans not in result:
#                         result.append(ans)
#                     k += 1
#                     j -= 1
#                 elif sum_ < 0:
#                     k += 1
#                 elif sum_ > 0:
#                     j -= 1
#         return result
                
        