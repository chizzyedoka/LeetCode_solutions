class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        for char in s:
            if char not in counter:
                counter[char] = 0
            counter[char] += 1

        for i in range(len(s)):
            char = s[i]
            if counter[char] == 1:
                return i

        return -1