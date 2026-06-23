class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # we need 2 states, one for the position in text1 nd the other in position in text2
        # the function dp(i,j) will represent the longest subsequence btw text1[i:] and text2[j:]
        # dp(0,0) will give the answer to the question

        # for the recurrence equation, we get to decide to pick either text1[i] or text2[j] 
        # when text1[i] == text2[j] the equation becomes
        # dp(i, j) = 1 + 1+dp(i+1, j+1) 
        # but if not max(dp(i+1, j), dp(i, j+1))

        # base case
        # if i or j has exceeded the length of text1 or text2 return 0

        m = len(text1)
        n = len(text2)
        memo = {}
        def dp(i, j):
            if i == m or j == n:
                return 0
            
            if (i,j) not in memo:
                if text1[i] == text2[j]:
                    memo[(i,j)] = 1+dp(i+1, j+1)                
                else:
                    memo[(i,j)] =  max(dp(i+1, j), dp(i, j+1))
            return memo[(i,j)]

        return dp(0,0)
            
