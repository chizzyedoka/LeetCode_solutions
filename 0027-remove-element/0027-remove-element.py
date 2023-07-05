class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        current = 0
        start = 0
        while start < len(nums):
            if nums[current] != val:
                nums[k] = nums[current]
                k += 1
            current += 1
            start += 1
        return k
        