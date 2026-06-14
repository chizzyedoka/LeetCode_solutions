class Solution:
    def rob(self, nums: List[int]) -> int:
        # if there's just one house, pick that
        # if there's just two houses, pick the max btw first and second house
        # if there's three houses we can either choose to rob the first and third house or just the second house 
        # dp[3] = max(dp[1]+nums[3], dp[2])

        # if there's four houses
        # dp[4] = max(nums[4] + dp[2], dp[3])
        # where dp[i] is the max money a robber can steal at house i

        # [1, 2, 3, 1]
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n 
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1]) 

        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[n-1]