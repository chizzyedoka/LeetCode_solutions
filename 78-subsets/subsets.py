class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
#                      *
#             /                \
#             [1]                [] 1
#          /    \              /    \
#     [1,2]     [1]           [2]     []   2
#     /  \        /\           / \      / \
# [1,2,3] [1,2]  [1,3] [1]  [2,3] [2]  [3] [] 
        result = []
        solution= []
        n = len(nums)
        def backtrack(i):
            if i == n:
                result.append(solution.copy())
                return

            solution.append(nums[i])
            backtrack(i+1)
            solution.pop()
            backtrack(i+1)

        backtrack(0)
        return result



