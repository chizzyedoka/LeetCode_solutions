# iterative
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        source, target = 0, n-1
        stack = [( source, [source] )]
        allPaths = []
        while stack:
            node, path = stack.pop()
            if node == target:
                allPaths.append(path)
            for nei in graph[node]:
                stack.append((nei, path + [nei]))
        return allPaths

# dfs
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        source, target = 0, n-1
        allPaths = []
        
        def dfs(node, path): 
            if node == target:
                allPaths.append(path)
                return

            for nei in graph[node]:
                if dfs(nei, path + [nei]):
                    return
            return

        dfs(source, [source])
        return allPaths

# queue
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        source, target = 0, n-1
        queue = deque([( source, [source] )])
        allPaths = []
        while queue:
            node, path = queue.popleft()
            if node == target:
                allPaths.append(path)
            for nei in graph[node]:
                queue.append((nei, path + [nei]))
        return allPaths

#
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:  
        n = len(graph)
        source, target = 0, n-1
        allPaths = []
        
        def backtrack(node, path):
            if node == target:
                allPaths.append(path[:])
                return

            for neighbor in graph[node]:
                path.append(neighbor)
                backtrack(neighbor, path)
                path.pop()

            return

        backtrack(source, [source])

        return allPaths

