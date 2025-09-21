class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutation = []
        result = []
        n =  len(nums)

        def backtrack():
            if len(permutation) == n:
                result.append(permutation[:])
                return
            
            for num in nums:
                if num not in permutation:
                    permutation.append(num)
                    backtrack()
                    permutation.pop()

        backtrack()
        return result