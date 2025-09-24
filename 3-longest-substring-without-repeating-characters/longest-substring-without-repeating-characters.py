class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start = 0
        longestSubstring = 0

        for end in range(len(s)):
            char = s[end]
            while char in seen:
                seen.remove(s[start])
                start += 1
            seen.add(char)
            window_length = end - start + 1
            longestSubstring = max(longestSubstring, window_length)

        return longestSubstring