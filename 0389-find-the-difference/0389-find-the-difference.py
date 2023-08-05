class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        if len(s) > 1:
            for i in range(len(t)-1):
                if s[i] != t[i]:
                    return t[i]
            return t[-1]
        return t[0]
            
        