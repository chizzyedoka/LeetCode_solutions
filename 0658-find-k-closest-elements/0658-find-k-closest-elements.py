class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        maxHeap = []
        res = []
        for num in arr:
            heapq.heappush(maxHeap,(abs(num-x), num))
        while k>0:
            dist,value = heapq.heappop(maxHeap)
            res.append(value)
            k-=1
        res.sort()
        return res