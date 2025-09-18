class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def graphFormation(courses):
            graph = defaultdict(list)
            for (u,v) in courses:
                graph[u].append(v)
            return graph

        def dfs(node):
            state = states[node]
            if state == VISITING:
                return False
            elif state ==VISITED:
                return True

            states[node] = VISITING
            for i in graph[node]:
                if not dfs(i):
                    return False
            
            states[node] = VISITED
            return True


        graph = graphFormation(prerequisites)
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [0] * numCourses
        

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
