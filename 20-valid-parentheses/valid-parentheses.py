class Solution:
   # (((  )))
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', ']':'[', '}':'{'}
        stack = []

        for char in s:
            if char in brackets:
                closingBracket = char
                if stack and brackets[closingBracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                openBracket = char
                stack.append(openBracket)
        return len(stack) == 0
