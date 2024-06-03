class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Initialize the graph
        # graph = defaultdict(set)
        # for node1, node2 in edges:
        #     graph[node1].add(node2)
        #     graph[node2].add(node1)
        graph = {}
        for u,v in edges:
            if u not in graph:
                graph[u] = set()
            if v not in graph:
                graph[v] = set()
            graph[u].add(v)
            graph[v].add(u)
            
        visited = set()
        stack = [source]
        
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                if node == destination:
                    return True
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        return False
            