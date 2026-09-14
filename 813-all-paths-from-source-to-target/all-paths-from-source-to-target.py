class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []

        source, dest = 0, len(graph) -1
        path = [source]
        stack = [(source, path)]
        result = []

        while stack:
            (node, path) = stack.pop()
            if node == dest:
                result.append(path)

            for next_node in graph[node]:
                stack.append((next_node, path + [next_node]))
        return result

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        source, target = 0, len(graph)-1
        paths = []

        def dfs(node, path):
            path.append(node)
            if node == target:
                paths.append(list(path))
            else:
                for next_node in graph[node]:
                    dfs(next_node, path)
            path.pop()

        dfs(source, [])
        return paths