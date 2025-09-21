class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutation = []
        result = []
        n = len(nums)
        used = [False] * n
        nums.sort()

        def backtrack():
            if len(permutation) == n:
                result.append(permutation[:])
                return

            for i,num in enumerate(nums):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                permutation.append(num)
                backtrack()
                permutation.pop()
                used[i] = False
                
        backtrack()
        return result
