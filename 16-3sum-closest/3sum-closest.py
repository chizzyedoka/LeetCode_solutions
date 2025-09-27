class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closet_sum = float("inf")
        for i in range(len(nums)):
            l, r = i +1, len(nums)-1
            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                if abs(cur_sum - target) < abs(closet_sum-target):
                    closet_sum = cur_sum
                if cur_sum > target:
                    r-=1
                elif cur_sum < target:
                    l += 1
                else:
                    return target
        return closet_sum