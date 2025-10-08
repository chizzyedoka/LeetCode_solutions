class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = 1
        right_product = 1
        n = len(nums)

        left_arr = [1] * n
        right_arr = [1] * n

        for i in range(n):
            left_arr[i] = left_product
            left_product = left_product * nums[i]

        for j in range(n-1,-1,-1):
            right_arr[j] = right_product
            right_product = right_product * nums[j]

        return [left_arr[i]* right_arr[i] for i in range(n)]