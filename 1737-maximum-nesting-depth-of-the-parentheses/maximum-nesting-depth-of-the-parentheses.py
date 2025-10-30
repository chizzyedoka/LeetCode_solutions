class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        depth = 0
        max_depth = 0

        for char in s:
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
            max_depth = max(depth, max_depth)
        return max_depth