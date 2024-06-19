class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        nums.sort()
        def backtrack(counter):
            if len(sol)==len(nums):
                res.append(sol[:])
                return
            for num in counter:
                if counter[num] > 0:                  
                    sol.append(num)
                    counter[num] -=1 
                    backtrack(counter)
                    sol.pop()
                    counter[num] += 1
        backtrack(Counter(nums))
        return res