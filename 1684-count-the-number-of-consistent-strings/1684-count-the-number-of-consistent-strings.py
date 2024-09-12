class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = len(words)
        allowed = set(allowed)
        for word in words:
            for char in word:
                if char not in allowed:
                    count -= 1
                    break
        return count