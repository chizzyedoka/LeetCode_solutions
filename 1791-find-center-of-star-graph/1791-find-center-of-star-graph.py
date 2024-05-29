class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        seen = {}
        for u,v in edges:
            if u not in seen:
                seen[u] = True
            elif u in seen:
                return u
            if v not in seen:
                seen[v] = True
            elif v in seen:
                return v