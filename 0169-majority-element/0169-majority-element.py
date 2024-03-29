# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         hashMap = {}
#         my_max = float('-inf')
#         if len(nums) == 1:
#             return nums[0]
#         for i in range(len(nums)):
#             if nums[i] not in hashMap:
#                 hashMap[nums[i]] = 0
#             hashMap[nums[i]] += 1
#             if hashMap[nums[i]] > my_max:
#                     my_max,result = hashMap[nums[i]],nums[i]
#         return result
            
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate