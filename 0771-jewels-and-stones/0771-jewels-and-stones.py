class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        no_of_jewels = 0
        for s in stones:
            if s in jewels:
                no_of_jewels += 1
        return no_of_jewels