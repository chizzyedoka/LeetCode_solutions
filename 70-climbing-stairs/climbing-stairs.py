class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        if n=1, we can climb in one distinct way
        if n=2, we can climb in 2 distinct way -> take 1 step twice or take 2 steps once
        if n=3, we can take 1step three times till we get to the top,
                or take 1step first then 2step later,
                or take 2steps first then 1step later
                that's 3 distinct ways
        if n=4, we can take 1 step till we get to the top,
                1 step two times, 2 step once
                1 step, 2 step, 1step
                2 step twice
                2 step, 1step twice

        if n=5, 1step each till the top
                1step 3 times, 2step once
                1step 2 times, 2step once, 1 step
                1 step 1 time, 2 step once, 1step, 1step
                1 step 1 time, 2 step once, 2 step once
                2 step twice, 1step
                2 step once, 1step, 1step, 1syep
        n=1-> 1
        n=2 -> 2
        n=3 -> 3
        n=4 -> 5
        n=5 -> 8
        """
        memo = {}
        def dp(n):
            if n<=2:
                return n
            if n not in memo:
                memo[n] = dp(n-1) + dp(n-2)
            return memo[n]
        return dp(n)


        