class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for (u,v) in edges:
            graph[u].append(v)
            graph[v].append(u)

        if source == destination:
            return True

        if source not in graph:
            return False
        if destination not in graph:
            return False
        
        seen = set()

        def dfs(node, target):
            if node == target:
                return True
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    if dfs(neighbor, target):
                        return True
        
        for node in graph:
            if node == source:
                if dfs(node, destination):
                    return True
        return False