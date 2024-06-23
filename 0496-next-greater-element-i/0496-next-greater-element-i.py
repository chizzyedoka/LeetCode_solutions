class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def greater(n, nums):
            seen = False
            for num in nums:
                if n == num:
                    seen = True
                if num > n and seen:
                    return num
            return -1
        res = []
        for num in nums1:
            res.append(greater(num, nums2))
        return res
            