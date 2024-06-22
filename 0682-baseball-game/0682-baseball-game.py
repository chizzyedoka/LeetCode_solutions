class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for val in operations:
            if val == "C":
                stack.pop()
            elif val == "D":
                new_val = (stack[-1]) * 2
                stack.append(new_val)
            elif val == "+":
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(val))
        return sum(stack)
        # print(stack)
        # ans = 0
        # if len(stack) == 0:
        #     return ans
        # for val in stack:
        #     ans += int(val)
        # return ans
            