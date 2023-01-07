class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank, curr_tank = 0,0
        starting_index = 0
        for i in range(len(gas)):
            remaining = gas[i] - cost[i]
            total_tank += remaining
            curr_tank += remaining
            if curr_tank < 0:
                starting_index = i + 1
                curr_tank = 0
        return starting_index if total_tank >= 0 else -1
        