import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim's algorithm to create a MST (Minimum Spanning Tree)
        n = len(points)
        total_cost = 0
        heap = [(0, 0)]
        seen = set()

        while len(seen) < n:
            dist, i = heapq.heappop(heap)
            if i in seen:
                continue
            
            seen.add(i)
            total_cost += dist
            xi, yi = points[i]

            for j in range(n):
                if j not in seen:
                    xj, yj = points[j]
                    nei_dist = abs(xi-xj) + abs(yi-yj)
                    heapq.heappush(heap, (nei_dist, j))
        
        return total_cost
                    
        # Time: O(n^2 log(n)) where n is the number of points
        #    or O(E log(E)) where E is the number of edges, which is n^2
        # Space: O(n^2) or O(E)



# import heapq
# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         n = len(points)

#         # Priority queue to store the edges with their costs
#         min_heap = []

#         # Function to calculate Manhattan distance
#         def manhattan_dist(p1, p2):
#             return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

#         # Add all edges from the first point (0) to the heap
#         for i in range(1, n):
#             dist = manhattan_dist(points[0], points[i])
#             heapq.heappush(min_heap, (dist, 0, i))

#         total_cost = 0
#         visited = set()
#         visited.add(0)

#         # While we have nodes to process in the heap
#         while len(visited) < n:
#             # Get the edge with the smallest weight
#             cost, u, v = heapq.heappop(min_heap)

#             # If the destination node has not been visited, add it to the MST
#             if v not in visited:
#                 visited.add(v)
#                 total_cost += cost

#                 # Add all edges from the new node to the heap
#                 for i in range(n):
#                     if i not in visited:
#                         dist = manhattan_dist(points[v], points[i])
#                         heapq.heappush(min_heap, (dist, v, i))

        return total_cost


