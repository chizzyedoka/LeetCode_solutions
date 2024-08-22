class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, res = 0, 0
        char_index = {}
        for end in range(len(s)):
            char = s[end]
            if char in char_index:
                # shrink the window
                start = max(start, char_index[char] + 1)
            char_index[char] = end
            res = max(res, end - start + 1)
        return res