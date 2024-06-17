class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)
        def backtrack():
            if len(sol) == n:
                res.append(sol[:])
                return
            for i in range(n):
                if nums[i] not in sol:
                    sol.append(nums[i])
                    backtrack()
                    sol.pop()
        backtrack()
        return res
            


# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         def backtrack(start):
#             # If we've reached the end of the array, add a copy of nums to result
#             if start == len(nums):
#                 res.append(nums[:])
#             for i in range(start, len(nums)):
#                 # Swap the current element with the start element
#                 nums[start], nums[i] = nums[i], nums[start]
#                 # Recurse with the next position as the new start
#                 backtrack(start + 1)
#                 # Backtrack by swapping the elements back
#                 nums[start], nums[i] = nums[i], nums[start]

#         backtrack(0)
#         return res





