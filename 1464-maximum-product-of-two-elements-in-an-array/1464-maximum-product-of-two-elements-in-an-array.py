class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        import heapq
        nums = [-num for num in nums]
        heapq.heapify(nums)
        i = -1*heapq.heappop(nums)
        j = -1*heapq.heappop(nums)
        return (i-1)*(j-1)