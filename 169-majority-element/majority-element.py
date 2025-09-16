class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        major_el = nums[0]

        for num in nums:
            if num == major_el:
                count += 1
            elif num != major_el:
                count -= 1
            if count == 0:
                major_el = num
                count += 1
        return major_el
