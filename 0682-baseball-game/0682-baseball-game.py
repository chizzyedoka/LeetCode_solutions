class Solution:
            
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operand in operations:
            if operand.lstrip('-').isdigit():
                stack.append(int(operand))
            elif operand == '+':
                prev = stack[-1]
                pprev = stack[-2]
                stack.append(prev+pprev)
            elif operand == 'D':
                temp = stack[-1]
                stack.append(temp*2)
            elif operand == 'C':
                stack.pop()
            print(stack)
        return sum(stack)