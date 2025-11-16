class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        n = len(s)
        
        def backtrack(i, solution):
            if i == n:
                result.append(solution)
                return

            char = s[i]
            if not char.isdigit():
            #pick
                backtrack(i+1, solution[:i] + char.upper() + solution[i+1:])
                backtrack(i+1, solution[:i] + char.lower() + solution[i+1:])

            # dont pick
            else:
                backtrack(i+1, solution+char)

        
        backtrack(0, "")
        return result