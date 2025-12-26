class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(' : ')',
            '{' : '}', 
            '[' : ']'
        }
        stack = [] # 

        for char in s:
            if char not in brackets and char not in brackets.values():
                return False
            if char in brackets:
                stack.append(char)
            else:
                if not stack:
                    return False
                elif brackets[stack[-1]] != char:
                    return False
                stack.pop()
        return len(stack) == 0 
            