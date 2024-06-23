class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        stack = [nums2[0]]
        res = []
        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1]:
                hashmap[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
        for num in nums1:
            res.append(hashmap.get(num,-1))
        return res


# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         def greater(n, nums):
#             seen = False
#             for num in nums:
#                 if n == num:
#                     seen = True
#                 if num > n and seen:
#                     return num
#             return -1
#         res = []
#         for num in nums1:
#             res.append(greater(num, nums2))
#         return res
            