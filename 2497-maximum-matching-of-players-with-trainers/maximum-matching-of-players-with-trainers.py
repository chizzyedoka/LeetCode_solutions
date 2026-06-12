class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        if not players or not trainers:
            return 0
        
        result = 0
        players.sort()
        trainers.sort()

        i = j = 0
        # 4, 7, 9
        # 2, 5, 8, 8

        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                i += 1
                j += 1
                result += 1
            else:
                j += 1

        return result
