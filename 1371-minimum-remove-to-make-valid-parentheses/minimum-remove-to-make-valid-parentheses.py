class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # 1. cant start with a closed parethesis )
        # 2. cant end with a open parenthesis (
        # 3. number of open has to be equal to number of closed
        
        if not s:
            return ""
        s = list(s)
        stack = [] # for storing index of open parenthesis

        for i,char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if not stack:
                    s[i] = ""
                else:
                    stack.pop()

        # there can be open parenthesis left without matching closed parenthesis
        while stack:
            position = stack.pop()
            s[position] = ""

        return "".join(s)
