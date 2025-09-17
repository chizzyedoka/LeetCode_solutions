class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dp(n, combination, start):
            if n == 0:
                result.append(combination[:])
                return result
            elif n < 0:
                return

            for i in range(start,len(candidates)):
                num = candidates[i]
                combination.append(num)
                dp(n-num, combination, i)
                combination.pop()
            return

        dp(target, [], 0)
        return result

