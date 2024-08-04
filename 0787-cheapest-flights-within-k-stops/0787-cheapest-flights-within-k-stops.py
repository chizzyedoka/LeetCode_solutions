import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {node:[] for node in range(n)}
        for u,v,w in flights:
            graph[u].append((v,w))
       
        shortest = {}
        minHeap = [(0, src, 0)]  
        
        while minHeap:
            w1, n1, stops = heapq.heappop(minHeap)
            if n1 == dst:
                return w1
            
            if stops > k:
                continue
                
            if (n1, stops) in shortest and shortest[(n1, stops)] <= w1:
                continue
                
            shortest[(n1, stops)] = w1
            for n2, w2 in graph[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, (w1+w2, n2, stops+1) )
        return -1