class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        next_row = [1]*(n-1)
        for i in range(n-1):
            next_row[i] = (nums[i] + nums[i+1]) % 10
        return self.triangularSum(next_row)
            
# class Solution:
#     def triangularSum(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 1:
#             return nums[0]
#         next_row = [nums[i] + nums[i + 1] for i in range(n - 1)]
#         return self.triangularSum(next_row)