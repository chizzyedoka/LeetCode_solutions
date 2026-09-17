class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED] * numCourses

        for (u,v) in prerequisites:
            graph[u].append(v)

        def dfs(node):
            if states[node] == VISITING:
                return False
            if states[node] == VISITED:
                return True

            states[node] = VISITING

            for new_node in graph[node]:
                if not dfs(new_node):
                    return False
            states[node] = VISITED
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True