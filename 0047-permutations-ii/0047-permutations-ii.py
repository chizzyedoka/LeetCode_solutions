class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        counter = {}
        for n in nums:
            if n not in counter:
                counter[n] = 0
            counter[n] += 1
    
        def backtrack():
            if len(sol)==len(nums):
                res.append(sol[:])
                return
            for num in counter:
                if counter[num] > 0:                  
                    sol.append(num)
                    counter[num] -=1 
                    backtrack()
                    sol.pop()
                    counter[num] += 1
        backtrack()
        return res