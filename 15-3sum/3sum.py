class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, n-1
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]

                if curr_sum == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif curr_sum > 0:
                    k -= 1
                else:
                    j += 1

        return result
