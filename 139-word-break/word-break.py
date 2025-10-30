# brute force -> 2**n
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
    
        def dfs(start):
            if start == len(s):
                return True

            for end in range(start+1, len(s)+1):
                prefix = s[start:end]
                if prefix in wordDict and dfs(end):
                    return True
            return False

        return dfs(0)

# top-down dp
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = {}
    
        def dfs(start):
            if start == len(s):
                return True

            if start in memo:
                return memo[start]

            for end in range(start+1, len(s)+1):
                prefix = s[start:end]
                if prefix in wordDict and dfs(end):
                    memo[start] = True
                    return True
            memo[start] = False
            return False

        return dfs(0)

# bottom up
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                prefix = s[j:i]
                if dp[j] and prefix in wordDict:
                    dp[i] = True
                    break
        return dp[n]


# Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()
        for word in wordDict:
            current_node = root
            for char in word:
                if char not in current_node.children:
                    current_node.children[char] = TrieNode()
                current_node = current_node.children[char]
            current_node.isEndOfWord = True

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n):
            if not dp[i]:
                continue
            current_node = root
            for j in range(i, n):
                char = s[j]
                if char not in current_node.children:
                    break
                current_node = current_node.children[char]
                if current_node.isEndOfWord:
                    dp[j+1] = True
        return dp[-1]

                