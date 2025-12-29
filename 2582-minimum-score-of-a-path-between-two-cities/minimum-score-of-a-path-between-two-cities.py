class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        seen = set()
        graph = defaultdict(list) # {1:[(2,9)],    2:[(1,9)]}
        self.result = float("inf")

        for (u, v, w) in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))

        def dfs(node):
            seen.add(node)

            for next_node, weight in graph[node]:
                self.result = min(self.result, weight)
                if next_node not in seen:
                    dfs(next_node)

        

        dfs(1)
        return self.result

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        seen = set()
        graph = defaultdict(list) 
        self.result = float("inf")

        for (u, v, w) in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))

        queue = deque([1])
        while queue:
            node = queue.popleft()
            seen.add(node)
            for next_node, weight in graph[node]:
                self.result = min(self.result, weight)
                if next_node not in seen:
                    queue.append(next_node)

        return self.result


        


        