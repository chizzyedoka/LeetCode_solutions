class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        def helper_reverse(arr,left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        helper_reverse(nums, 0, n-1)
        helper_reverse(nums, 0,k-1)
        helper_reverse(nums,k, n-1)