class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        if len(players) < 1 or len(trainers) < 1:
            return 0
        players.sort()
        trainers.sort()
        i, j = 0,0
        count = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                count += 1
                i += 1
            j += 1
        return count
            
        