
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def backtrack(node, path):
            if node == len(graph) - 1:
                # If we've reached the target node, add the path to the results
                res.append(list(path))
                return
            
            # Explore each neighbor of the current node
            for neighbor in graph[node]:
                path.append(neighbor)
                backtrack(neighbor, path)
                path.pop()  # Backtrack to explore other paths

        res = []
        backtrack(0, [0])  # Start the backtracking from node 0 with path [0]
        return res

        