import heapq as h
class MedianFinder:

    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def addNum(self, num: int) -> None:
        h.heappush(self.maxHeap, -num)
        top = h.heappop(self.maxHeap)
        h.heappush(self.minHeap, -top)
        if len(self.minHeap) > len(self.maxHeap):
            h.heappush(self.maxHeap,-1*h.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -1*self.maxHeap[0]
        return (-1*self.maxHeap[0] + self.minHeap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()