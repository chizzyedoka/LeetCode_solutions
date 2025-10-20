class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        string_builder = []
        result = []
        balance = 0
        for char in s:
            if char == "(":
                balance += 1
                string_builder.append(char)
            elif char == ")" and balance > 0:
                string_builder.append(")")
                balance -= 1
            elif char != ")":
                string_builder.append(char)

        for i in range(len(string_builder)-1, -1, -1):
            char = string_builder[i]
            if char == "(" and balance > 0:
                balance -= 1
            else:
                result.append(char)

        return "".join(result[::-1])