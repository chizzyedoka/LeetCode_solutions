class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        res = 0
        def binSearch(l, r , t):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= t:
                    l = mid + 1
                else:
                    r = mid - 1
            return r
                    
        for left in range(len(nums)):
            right = binSearch(left, len(nums)-1 , target - nums[left]) 
            if right >= left:
                res += (2**(right-left)) % MOD
        return res % MOD