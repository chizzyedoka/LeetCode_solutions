class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float("inf")
        result = 0

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]

                if abs(target - cur_sum) < diff:
                    diff = abs(target - cur_sum)
                    result = cur_sum
                if cur_sum < target:
                    j += 1
                else:
                    k -= 1
        return result