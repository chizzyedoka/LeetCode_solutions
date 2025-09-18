class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        def graph_formation(courses):
            graph = defaultdict(list)
            for (u,v) in courses:
                graph[u].append(v)  
            return graph

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses
        path = []

        def dfs(node):
            state = states[node]
            if state == VISITED:
                return True
            elif state == VISITING:
                return False  

            states[node] = VISITING

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            states[node] = VISITED  
            path.append(node)
            return True

        graph = graph_formation(prerequisites)

        for node in range(numCourses):
            if not dfs(node):
                return []
        return path
