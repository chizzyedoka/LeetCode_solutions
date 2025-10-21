class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(start, destination, weight):
            if start == destination:
                return weight
            seen.add(start)
            for neighbor, val in graph[start]:
                if neighbor not in seen:
                    result = dfs(neighbor, destination, weight*val)
                    if result != -1:
                        return result
            return -1

        result = []
        graph = defaultdict(list)

        for i in range(len(equations)):
            u,v = equations[i]
            graph[u].append((v, values[i]))
            graph[v].append((u, 1/values[i]))

        for query in queries:
            start, destination = query
            if start in graph and destination in graph:
                seen = set()
                answer = dfs(start, destination, 1)
                result.append(answer)
            else:
                result.append(-1)
        return result

        