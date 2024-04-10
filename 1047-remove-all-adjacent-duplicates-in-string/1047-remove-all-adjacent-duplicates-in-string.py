class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s) < 1:
            return s
        stack = []
        for i in range(len(s)):
            if len(stack) > 0 and s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        res = ""
        while len(stack) > 0:
            char = stack.pop()
            res += char
        return res[::-1]