class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap = [] # we will be using a maxHeap
        stops = 0

        # add the target as last position with  0 fuel
        stations.append([target, 0])
        tank = startFuel
        prev = 0

        for distance, fuel in stations:
            tank -= distance - prev
            
            # if we cant reach this station, refuel with the best past station(s)
            while heap and tank < 0:
                tank += -1*heapq.heappop(heap)
                stops += 1

            if tank < 0: # even after refueling, can't reach
                return -1
            
            
            heapq.heappush(heap, -fuel)
            prev = distance
        return stops
        