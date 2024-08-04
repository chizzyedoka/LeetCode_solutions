import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # Priority queue to store the edges with their costs
        min_heap = []

        # Function to calculate Manhattan distance
        def manhattan_dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        # Add all edges from the first point (0) to the heap
        for i in range(1, n):
            dist = manhattan_dist(points[0], points[i])
            heapq.heappush(min_heap, (dist, 0, i))

        total_cost = 0
        visited = set()
        visited.add(0)

        # While we have nodes to process in the heap
        while len(visited) < n:
            # Get the edge with the smallest weight
            cost, u, v = heapq.heappop(min_heap)

            # If the destination node has not been visited, add it to the MST
            if v not in visited:
                visited.add(v)
                total_cost += cost

                # Add all edges from the new node to the heap
                for i in range(n):
                    if i not in visited:
                        dist = manhattan_dist(points[v], points[i])
                        heapq.heappush(min_heap, (dist, v, i))

        return total_cost


