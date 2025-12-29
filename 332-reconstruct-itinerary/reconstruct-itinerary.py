class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        n = len(tickets)
        result = []

        for i in range(n):
            fromPort, toPort = tickets[i]
            graph[fromPort].append(toPort)

        for node in graph:
            graph[node].sort(reverse=True)

        def dfs(node):
            while graph[node]:
                next_node = graph[node].pop()
                dfs(next_node)
            result.append(node)


        dfs("JFK")
        return result[::-1]
