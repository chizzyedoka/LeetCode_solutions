from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        # Initialize the graph
        graph = defaultdict(set)
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)
            
        # BFS to check if there is a path from start to end
        queue = deque([start])
        visited = set([start])
        
        while queue:
            currentNode = queue.popleft()
            if currentNode == end:
                return True
            for neighbor in graph[currentNode]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return False

