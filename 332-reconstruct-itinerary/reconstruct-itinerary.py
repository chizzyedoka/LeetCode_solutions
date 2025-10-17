from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        
        # use min-heap to keep lexical order without re-sorting
        for u, v in tickets:
            heapq.heappush(graph[u], v)
            
        result = []

        def dfs(node):
            while graph[node]:
                # always take the smallest lexical neighbor
                next_node = heapq.heappop(graph[node])
                dfs(next_node)
            result.append(node)
        
        dfs("JFK")
        return result[::-1]
