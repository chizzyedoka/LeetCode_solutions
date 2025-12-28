class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        source, target = 0, len(graph)-1
        paths = []

        def dfs(node, path):
            if node == target:
                paths.append(list(path))
                return
            
            for next_node in graph[node]:
                path.append(next_node)
                dfs(next_node, path)
                path.pop()

        dfs(source, [0])
        return paths