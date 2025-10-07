class Solution:
    def isPalindrome(self,s, i, j):
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        current_partition = []

        def dfs(i):
            if i >= len(s):
                res.append(current_partition.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s,i, j):
                    current_partition.append(s[i:j+1])
                    dfs(j+1)
                    current_partition.pop()

        dfs(0)
        return res
            
