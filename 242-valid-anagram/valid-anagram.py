class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_bucket = [0] * 26
        t_bucket = [0] * 26

        for i in range(len(s)):
            s_char, t_char = s[i], t[i]
            s_index = ord(s_char) - ord('a')
            t_index = ord(t_char) - ord('a')
            s_bucket[s_index] += 1
            t_bucket[t_index] += 1

        for i in range(26):
            if s_bucket[i] != t_bucket[i]:
                return False

        return True
