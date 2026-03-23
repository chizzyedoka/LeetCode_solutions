class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        start = 0
        seen = set()
        result = 0

        for end in range(n):
            char = s[end]
            while char in seen:
                seen.remove(s[start])
                start += 1
            else:
                seen.add(char)
                window = end - start + 1
                result = max(result, window)
        return result