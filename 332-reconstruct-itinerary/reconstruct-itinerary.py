from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        # Build graph
        for u, v in tickets:
            graph[u].append(v)

        # Sort once, in reverse order, so we can pop from the end in O(1)
        for u in graph:
            graph[u].sort(reverse=True)

        result = []

        def dfs(node):
            # explore while there are outgoing edges
            while graph[node]:
                next_node = graph[node].pop()  # O(1)
                dfs(next_node)
            result.append(node)

        dfs("JFK")
        return result[::-1]
