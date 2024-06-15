class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(s, left, right):
            if len(s) == n * 2:
                res.append(s)
                return 
            
            if left < n:
                #s += "("
                #left += 1
                dfs(s+"(", left+1, right)
                
            if right < left:
                #s += ")"
                #right += 1
                dfs(s+")", left, right+1)
                
        dfs("", 0, 0)
        return res