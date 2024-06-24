class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        num = 0
        result = 0
        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char == '+':
                result += sign*num 
                num = 0
                sign = 1
            elif char == '-':
                result += sign*num
                num = 0
                sign = -1
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                result += sign*num
                num = 0
                result *= stack.pop()
                result += stack.pop()
        result += sign*num
        return result