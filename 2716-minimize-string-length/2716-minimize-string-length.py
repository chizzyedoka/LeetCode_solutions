class Solution:
    def minimizedStringLength(self, s: str) -> int:
        seen = set()
        for char in s:
            if char not in seen:
                seen.add(char)
        return len(seen)     