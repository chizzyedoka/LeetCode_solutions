# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         subsets = []
#         subsets.append([])
#         for char in nums:
#             n = len(subsets)
#             for i in range(n):
#                 myset = list(subsets[i])
#                 myset.append(char)
#                 subsets.append(myset)
#         return subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]  # Start with the empty subset
        
        for num in nums:
            new_subsets = []
            for subset in res:
                new_subsets.append(subset + [num])  # Add current num to each subset
            res += new_subsets  # Add the new subsets to the result list
        
        return res
