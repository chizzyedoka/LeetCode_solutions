class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            correct_index = nums[i] 
            if ((nums[i] < len(nums))and nums[i] != nums[correct_index]):
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1
                
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
#         n = len(nums) + 1
#         # x1 represents the XOR of all v alues from 1 to n
#         x1 = 1
#         for i in range(2, n+1):
#             x1 = x1 ^ i
        
#         # x2 represents XOR for all values in arr
#         x2 = nums[0]
#         for i in range(1, n):
#             x2 = x2 ^ nums[i]
        
#         return x1 ^ x2
        
        
        
        
#         numsSum = 0
#         maxNum = 0
            
#         for i in range(len(nums)):
#             numsSum += nums[i]
#             if nums[i] > maxNum:
#                 maxNum = nums[i]
#         expectedSum = sum((i for i in range(0,maxNum+1)))

#         return expectedSum - numsSum
        