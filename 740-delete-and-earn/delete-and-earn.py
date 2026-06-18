class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        # dp(i) function ? tells us the maximum points you can earn btw 0 and i
        # we need a hashmap of num and occurrence so we can know the gains from a num
        # when is it good to pick a number? when we loose less from delting nums[i-1] and nums[i] + 1
        # this means dp(i) = max(dp(i-2) + gain, dp(i-1))
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += num

        memo = {}
        max_num = max(nums)

        def dp(i):
            if i == 0:
                return 0
            if i == 1:
                return counter.get(1,0)
    
            if i not in memo:
                memo[i] = max(dp(i-1), counter.get(i,0) + dp(i-2))
            return memo[i]

        return dp(max_num)

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_num = float("-inf")
        
        points = {}
        for num in nums:
            max_num = max(max_num, num)
            if num not in points:
                points[num] = 0
            points[num] += num

        dp = [0] * (max_num+1)
        dp[1] = points[1] if 1 in points else 0

        for i in range(2, max_num+1):
            dp[i] = max(points.get(i, 0) + dp[i-2], dp[i-1])

        print(dp)
        return dp[max_num]