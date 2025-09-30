class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k):
            hours_taken = 0
            for pile in piles:
                hours_taken += ceil(pile/k)
            return hours_taken <= h

        l, r = 1, max(piles) + 1
        while l < r:
            k = (l+r) // 2
            if k_works(k):
                r = k
            else:
                l = k+ 1
        return r 
       
