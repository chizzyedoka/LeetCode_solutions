class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        maxCoin = 0
        i = 0
        piles.sort()
        for i in range(len(piles)//3,len(piles),2):
            maxCoin += piles[i]
        return maxCoin