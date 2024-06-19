class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(start, sol):
            res.append(sol[:])
            # pick
            for i in range(start,len(nums)):
                if i >start and nums[i] == nums[i-1]:
                    continue
                sol.append(nums[i])
                backtrack(i+1, sol)
                sol.pop()
                
        backtrack(0, [])
        return res
            
            
            

            
            