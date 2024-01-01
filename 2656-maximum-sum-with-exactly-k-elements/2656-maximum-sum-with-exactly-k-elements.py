class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxSum = nums[-1]
        while k > 1:
            m = nums[-1]
            nums[-1] = m + 1
            maxSum += nums[-1]
            k -= 1
        return maxSum