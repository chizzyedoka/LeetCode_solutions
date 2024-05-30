from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Initialize the adjacency list
        edges_map = {i: set() for i in range(n)}
        for u, v in edges:
            edges_map[u].add(v)
            edges_map[v].add(u)

        # If source is the same as destination, there is trivially a valid path
        if source == destination:
            return True
        
        # BFS to check if there is a path from source to destination
        queue = deque([source])
        visited = set()

        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            if node not in visited:
                visited.add(node)
                for neighbor in edges_map[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return False
