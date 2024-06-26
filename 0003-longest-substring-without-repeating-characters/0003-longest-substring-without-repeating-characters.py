# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         n = len(s)
#         ans = 0
#         # mp stores the current index of a character
#         mp = {}

#         i = 0
#         # try to extend the range [i, j]
#         for j in range(n):
#             if s[j] in mp:
#                 i = max(mp[s[j]], i)

#             ans = max(ans, j - i + 1)
#             mp[s[j]] = j + 1

#         return ans
    
    
    
    
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         substring = deque()
#         max_substring = 0
#         for char in s:
#             while char in substring:
#                 substring.popleft()
#             substring.append(char)
#             max_substring = max(max_substring, len(substring))
#         return max_substring

    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start, max_length = 0,0
        char_index = {}
        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char in char_index:
                window_start = max(window_start, char_index[right_char]+1)
            char_index[right_char] = window_end
            max_length = max(max_length, window_end-window_start+1)
        return max_length

                
                