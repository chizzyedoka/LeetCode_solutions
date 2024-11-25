class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        res = 0
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += (2**(r-l))
                l += 1
        return res % MOD