class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = dict()
        for i in range(len(nums)):
            value = target - nums[i]
            if value in  hashMap.keys():
                return [hashMap[value],i]
            hashMap[nums[i]] = i
           
#         pointer_one = 0
#         pointer_two = len(nums) - 1
#         hashMap = dict()
#         for index, num in enumerate(nums):
#             if num not in hashMap:
#                 hashMap[num] = []
#             hashMap[num].append(index)

#         nums = sorted(nums)

#         while pointer_one < pointer_two:
#             sum = nums[pointer_one] + nums[pointer_two]
#             if sum == target:
#                 if nums[pointer_one] == nums[pointer_two]:
#                     return [hashMap[nums[pointer_one]][0], hashMap[nums[pointer_two]][1]]
#                 return [hashMap[nums[pointer_one]][0], hashMap[nums[pointer_two]][0]]
#             elif sum < target:
#                 pointer_one += 1
#             else:
#                 pointer_two -= 1







        """ for i in range(len(nums)):
            for j in range(1,len(nums)):
                if i == j:
                    continue
                elif nums[i] == target - nums[j]:
                    return [i,j]
                    """
        
        