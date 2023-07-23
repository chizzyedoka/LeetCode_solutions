class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        minHeap = []
        heapq.heapify(nums)
        for i in range(len(nums)-k):
            minHeap.append(heapq.heappop(nums))
        print(nums)
        return nums[0] 
        