class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        n = len(word)
        start = 0
        result = 0
        seen = set()

        for end in range(1,n):
            if ord(word[end]) < ord(word[end-1]):
                start = end
                seen = set()
            else:
                seen.add(word[end])
                seen.add(word[end-1])
                if len(seen) == 5:
                    result = max(result, end-start+1)

        return result