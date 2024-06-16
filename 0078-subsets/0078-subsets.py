class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums) 
        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            
            # don't pick nums[i]
            backtrack(i+1)
            
            # pick nums[i]
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
            
        backtrack(0)
        return res
    
# backtracking    
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         def backtrack(start, path):
#             res.append(path)
#             for i in range(start, len(nums)):
#                 backtrack(i + 1, path + [nums[i]])
#         res = []
#         backtrack(0, [])
#         return res

