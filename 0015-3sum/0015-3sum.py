class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            left, right = i + 1, len(nums)-1
            while left < right:
                cur_sum = nums[left] + nums[right] + nums[i]
                if cur_sum < 0:
                    left += 1
                elif cur_sum > 0:
                    right -= 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                        continue
        return triplets