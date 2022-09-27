class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)): # loop through nums
            expected = target - nums[i]
            for j in range(i+1,len(nums)):
                if expected == nums[j]:
                    output.append(i)
                    output.append(j)
            """if expected in nums[i+1:]:
                output.append(i)"""
        return output
        