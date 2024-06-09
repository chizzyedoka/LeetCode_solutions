class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subsets.append([])
        for char in nums:
            n = len(subsets)
            for i in range(n):
                myset = list(subsets[i])
                myset.append(char)
                subsets.append(myset)
        return subsets