class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol, res = [], []
        n = len(candidates)
        candidates.sort()

        def backtrack(start, curSum):
            if curSum == target:
                res.append(sol.copy())
                return

            for i in range(start, n):
                if curSum + candidates[i] <= target:
                    sol.append(candidates[i])
                    backtrack(i, curSum + candidates[i])
                    sol.pop()

        backtrack(0, 0)
        return res






