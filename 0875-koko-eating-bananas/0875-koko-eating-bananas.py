class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def timeToFinish(k):
            time = 0
            for pile in piles:
                time += ceil(pile / k)
            return time
        
        l, r = 1, max(piles)
        while l < r:
            mid = (l+r) // 2
            t = timeToFinish(mid)
            if t <= h:
                r = mid 
            else:
                l = mid + 1
        return l
            