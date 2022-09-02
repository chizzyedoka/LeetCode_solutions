class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = {}
        for i in range(len(nums)):
            if nums[i] not in counter.keys():
                counter[nums[i]] = 1
            else:
                counter[nums[i]] += 1
        for key, value in counter.items():
            if value == 1:
                return key