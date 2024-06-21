class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k):
            hours = 0
            for pile in piles:
                hours += ceil(pile/k)
            return hours <= h
        l, r = 1, max(piles)
        
        # optimized
        while l < r:
            k = (l+r)//2
            if k_works(k):
                r = k
            else:
                l = k + 1
        return l
        
        # unoptimized
        # l, r = 1, max(piles)
        # for k in range(l, r+1):
        #     if k_works(k):
        #         return k
        