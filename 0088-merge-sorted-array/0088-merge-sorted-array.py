class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1, ptr2,ptr3 = m-1,n-1,m+n-1
        while ptr1 >= 0 and ptr2 >= 0:
            if nums1[ptr1] >= nums2[ptr2]:
                nums1[ptr3] = nums1[ptr1]
                ptr1 -= 1
                
            elif nums2[ptr2] > nums1[ptr1]:
                nums1[ptr3] = nums2[ptr2]
                ptr2 -= 1
            ptr3 -= 1
                
        while ptr2 >= 0:
            nums1[ptr3] = nums2[ptr2] 
            ptr2 -= 1
            ptr3 -= 1
        




                
        