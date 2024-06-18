class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the numbers to handle duplicates
        sol, res = [], []
        n = len(nums)

        def backtrack(start):
            res.append(sol[:])  # Add the current subset to the result
            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]:
                    continue  # Skip duplicates
                sol.append(nums[i])
                backtrack(i + 1)
                sol.pop()

        backtrack(0)
        return res



        