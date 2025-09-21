class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        memo = {}
        def getPowerValue(n):
            if n == 1:
                return 1
            if n%2 == 0:
                memo[n] = 1+getPowerValue(n/2)
            else:
                memo[n] = 1+getPowerValue(3*n + 1)
            return memo[n]

        powerValues = [(getPowerValue(num), num) for num in range(lo, hi+1)]
        powerValues.sort()
        return powerValues[k-1][1]