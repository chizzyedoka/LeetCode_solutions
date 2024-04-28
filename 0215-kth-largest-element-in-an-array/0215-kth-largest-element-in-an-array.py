class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # using a maxHeap
        import heapq
        maxHeap = [-num for num in nums ]
        heapq.heapify(maxHeap)
        for _ in range(k-1):
            heapq.heappop(maxHeap)
        return -maxHeap[0]
        
        # using a min heap
        # import heapq
#         minHeap = []
#         heapq.heapify(nums)
#         for i in range(len(nums)-k):
#             minHeap.append(heapq.heappop(nums))
#         return nums[0] 
        
        