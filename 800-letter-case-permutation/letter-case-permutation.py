class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []

        def backtrack(i, solution):
            if i == len(s):
                result.append(solution)
                return result
            
            char = s[i]
            if not char.isdigit():
                # pick
                if not char.isupper():
                    backtrack(i+1, solution + char)
                    backtrack(i+1, solution + char.upper())
                else:
                    backtrack(i+1, solution + char)
                    backtrack(i+1, solution + char.lower())

            else:
                backtrack(i+1, solution + char)

        backtrack(0, "")
        return result
