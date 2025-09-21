class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        result = []
        graph = defaultdict(list)
        
        for i, equation in enumerate(equations):
            u,v = equation
            graph[u].append((v,values[i]))
            graph[v].append((u,1/values[i]))

        def dfs(src,dest, weight):
            if src == dest:
                return weight

            seen.add(src)
            for neighbor, w in graph[src]:
                if neighbor not in seen:
                    res = dfs(neighbor, dest, w* weight) 
                    if res != -1:
                        return res
            return -1
           
                

        for query in queries:
            u,v = query
            if u not in graph or v not in graph:
                result.append(-1)
            else:
                seen = set()
                result.append(dfs(u,v, 1))

        return result