import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1,n+1)}
        for u, v, w in times:
            graph[u].append([v,w])
        shortest = {}
        minHeap = [[0, k]]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1
            for n2, w2 in graph[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w1+w2, n2])
        print(shortest)
        if len(shortest)==n:
            return max(shortest.values())
        return -1
      
    
# import heapq
# class Solution:
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#         # Create the adjacency list
#         graph = {i: [] for i in range(1, n + 1)}
#         for u, v, w in times:
#             graph[u].append([v, w])
        
#         # Initialize the shortest path dictionary and minHeap
#         shortest = {i: float('inf') for i in range(1, n + 1)}
#         shortest[k] = 0
#         minHeap = [[0, k]]
        
#         while minHeap:
#             w1, n1 = heapq.heappop(minHeap)
            
#             if w1 > shortest[n1]:
#                 continue
            
#             for n2, w2 in graph[n1]:
#                 if shortest[n1] + w2 < shortest[n2]:
#                     shortest[n2] = shortest[n1] + w2
#                     heapq.heappush(minHeap, [shortest[n2], n2])
        
#         # Find the maximum time required to reach all nodes
#         max_time = max(shortest.values())
        
#         # If there's a node that we couldn't reach, return -1
#         return max_time if max_time != float('inf') else -1

