# class Solution:
#     def findJudge(self, n: int, trust: List[List[int]]) -> int:
#         if not trust:
#             return n
#         graph = {}
#         possible = -1
#         for u, v in trust:
#             if u not in graph:
#                 graph[u] = []
#             graph[u].append(v)
#         for i in range(n):
#             if i+1 not in graph.keys():
#                 possible = i+1
#         for people in graph.values():
#             if possible not in people:
#                 possible = -1
#         return possible 

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        
        # Initialize trust counts
        trust_count = [0] * (n + 1)
        trusted_by_count = [0] * (n + 1)
        
        # Populate the trust arrays
        for a, b in trust:
            trust_count[b] += 1
            trusted_by_count[a] += 1
        
        # Find the judge
        for i in range(1, n + 1):
            if trust_count[i] == n - 1 and trusted_by_count[i] == 0:
                return i
        
        return -1

