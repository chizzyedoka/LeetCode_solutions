class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        if len(stones) == 0:
            return 0
        import heapq
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        while len(max_heap) > 1:
            y = heapq.heappop(max_heap)
            x = heapq.heappop(max_heap)
            #print(max_heap)
            if x != y:
                y = -y+x
                heapq.heappush(max_heap,-y)
        if len(max_heap) == 1:
            return -max_heap[0]
        return 0  
        
        