class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        import heapq
        min_heap = []
        for i in range(k):
            heapq.heappush(min_heap,nums[i])

        for i in range(k, len(nums)):
            if nums[i] > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap,nums[i])

        return min_heap[0]
        
        
        # using a maxHeap
        # import heapq
        # maxHeap = [-num for num in nums ]
        # heapq.heapify(maxHeap) # O(n)
        # for _ in range(k-1): #k
        #     heapq.heappop(maxHeap) #log(n)
        # return -maxHeap[0]
    # n + klogn
        
        # using a min heap
        # import heapq
#         minHeap = []
#         heapq.heapify(nums)
#         for i in range(len(nums)-k):
#             minHeap.append(heapq.heappop(nums))
#         return nums[0] 
        
        