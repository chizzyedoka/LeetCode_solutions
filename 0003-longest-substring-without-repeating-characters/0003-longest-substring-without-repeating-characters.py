class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans
    
    
    
    
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         count = 0
#         window = ""
#         longest = float("-inf")
        
#         for end in range(len(s)-1):
#             window += s[end]
#             if s[end+1] in window:
#                 window_len = len(window) 
#                 longest = max(longest,window_len)
#                 window = ""
             
                    
       #        if longest == float("-inf"):
#             return len(s)
#         return longest
                
                