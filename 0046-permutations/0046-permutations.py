# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         def backtrack(tempList: List[int]):
#             if len(tempList) == len(nums):
#                 res.append(tempList[:])
#             else:
#                 for num in nums:
#                     if num in tempList:
#                         continue
#                     tempList.append(num)
#                     backtrack(tempList)
#                     tempList.pop()
        
#         res = []
#         backtrack([])
#         return res


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start: int):
            # If we've reached the end of the array, add a copy of nums to result
            if start == len(nums):
                res.append(nums[:])
            for i in range(start, len(nums)):
                # Swap the current element with the start element
                nums[start], nums[i] = nums[i], nums[start]
                # Recurse with the next position as the new start
                backtrack(start + 1)
                # Backtrack by swapping the elements back
                nums[start], nums[i] = nums[i], nums[start]
        
        res = []
        backtrack(0)
        return res





