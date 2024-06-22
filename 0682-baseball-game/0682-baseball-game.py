class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for val in operations:
            if val != "C" and val != "D" and val != "+":
                stack.append(val)
            elif val == "C":
                stack.pop()
            elif val == "D":
                new_val = int(stack[-1]) * 2
                stack.append(new_val)
            elif val == "+":
                stack.append( int(stack[-1])+ int(stack[-2]) )
        print(stack)
        ans = 0
        if len(stack) == 0:
            return ans
        for val in stack:
            ans += int(val)
        return ans
            