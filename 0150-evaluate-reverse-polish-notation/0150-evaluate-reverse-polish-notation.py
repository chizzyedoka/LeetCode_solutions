class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '/', '*']
        stack = []
        for val in tokens:
            if val in operators:
                second = stack.pop()
                first = stack.pop()
                if val == '+':
                    stack.append(first+second)
                elif val == '-':
                    stack.append(first-second)
                elif val == '*':
                    stack.append(first*second)
                else:
                    div = first/second
                    if div < 0:
                        stack.append(ceil(div))
                    else:
                        stack.append(floor(div))
            else:
                stack.append(int(val))
        return stack[-1]