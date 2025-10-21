class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = {}

        def helper(index):
            if index in memo:
                return memo[index]
            if index == len(s):
                return [""]

            result = []
            for end in range(index + 1, len(s) + 1):
                word = s[index:end]
                if word in wordSet:
                    subs = helper(end)
                    for sub in subs:
                        result.append(word + (" " + sub if sub else ""))
            memo[index] = result
            return result

        return helper(0)
