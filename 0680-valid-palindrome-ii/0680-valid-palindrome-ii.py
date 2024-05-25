# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         left, right = 0, len(s) - 1
#         while left < right:
#             if s[left] != s[right]:
#                 one, two = s[left:right], s[left + 1:right + 1]
#                 return one == one[::-1] or two == two[::-1]
#             left, right = left + 1, right - 1
#         return True
    
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                r -= 1
                l+= 1
            return True
        l, r = 0, len(s)-1
        while l <= r:
            if s[l] != s[r]:
                return palindrome(l+1,r) or palindrome(l,r-1)
            r -= 1
            l+= 1
        return True