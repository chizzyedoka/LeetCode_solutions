class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        differences = []
        n = len(s1)
        for i in range(n):
            if s1[i] != s2[i]:
                differences.append(i)
                if len(differences) > 2: return False
        if not differences: return True
        if len(differences) == 2:
            i, j = differences
            return s1[i] == s2[j] and s1[j] == s2[i]
        return False