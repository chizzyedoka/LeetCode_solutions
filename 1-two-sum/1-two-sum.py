class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        
        
     
        output = []
        for i in range(len(nums)): # loop through nums
            expected = target - nums[i]
            for j in range(i+1,len(nums)):
                if expected == nums[j]:
                    return [i,j]
        return output
        
        