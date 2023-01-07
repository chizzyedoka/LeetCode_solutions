class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        total = 0
        output = 0
        if costs[0] > coins:
                return output
        for i in range(len(costs)):
            if total < coins:
                total += costs[i]
                output += 1
                if total > coins:
                    output -= 1
        return output
            
        