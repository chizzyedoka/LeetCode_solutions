class MedianFinder:

    def __init__(self):
        self.maxHeap = [] # smaller values
        self.minHeap = [] # larger values

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -1*num)
        # move the largest of the maxHeap to the minHeap
        val = -1* heapq.heappop(self.maxHeap)
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > len(self.maxHeap):
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1*val)

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -1*self.maxHeap[0]
        return (-1*self.maxHeap[0] + self.minHeap[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()