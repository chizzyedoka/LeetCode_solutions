class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = deque()
        result = 0
        for char in s:
            while char in seen:
                seen.popleft()
            else:
                seen.append(char)
                result = max(result, len(seen))
          

        return result