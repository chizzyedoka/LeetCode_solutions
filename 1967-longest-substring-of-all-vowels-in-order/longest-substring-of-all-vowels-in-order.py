class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        start = 0
        result = 0
        count = 1  # number of distinct vowels in order

        for end in range(1, len(word)):
            if word[end] < word[end - 1]:
                start = end
                count = 1
            elif word[end] > word[end - 1]:
                count += 1

            if count == 5:
                result = max(result, end - start + 1)

        return result