# brute force
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        n = len(s)
        result = []

        def dp(start, path): # dp(i) asks if we can split up to index i
            # base case
            if start == n:
                result.append(" ".join(path))
                return 

            for end in range(start+1, n+1):
                prefix = s[start:end]
                if prefix in wordDict:
                    path.append(prefix)
                    dp(end, path)

                    path.pop()
                    
                

        dp(0, [])

        return result

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        n = len(s)
        result = []

        def dp(start, path, result): # dp(i) asks if we can split up to index i
            # base case
            if start == n:
                sentence = " ".join(path)
                result.append(sentence)
                return

            for end in range(start+1, n+1):
                prefix = s[start:end]
                if prefix in wordDict:
                    path.append(prefix)
                    dp(end, path, result)

                    path.pop()

                    
                

        dp(0, [], result)

        return result
