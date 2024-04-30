class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # find the distance from origin for each points
        # put in max heap
        # pop k times
        import math
        import heapq
        max_heap = []
        res = []
        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(max_heap,(dist,point))
        for _ in range(k):
            d, point = heapq.heappop(max_heap)
            res.append(point)
        return res