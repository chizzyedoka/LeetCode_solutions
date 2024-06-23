class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # using stack
        s_copy = []
        while s:
            s_copy.append(s.pop())
        
        new_s = s_copy[::-1]
        while new_s:
            s.append(new_s.pop())
    
            

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         # using recursion
#         # create helper function
#         def helper(s,start,end):
#             if start > end:
#                 return s
#             # swap
#             s[start],s[end] = s[end], s[start]
#             helper(s,start+1,end-1)
#         helper(s,0,len(s)-1)
        
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
        # ptr_one = 0
        # ptr_two = len(s) - 1
        # temp = ['a'] * len(s)
        # while ptr_one < ptr_two:
        #     temp[ptr_one] = s[ptr_two]
        #     s[ptr_two] = s[ptr_one]
        #     s[ptr_one] = temp[ptr_one]
        #     ptr_one += 1
        #     ptr_two -= 1
        # return s 

    