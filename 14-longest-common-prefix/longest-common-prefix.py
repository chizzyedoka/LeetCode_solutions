class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = ""
        for i in range(len(strs[0])):
            char = strs[0][i]

            for word in strs[1:]:
                if i >= len(word) or char != word[i]:
                    return prefix
            prefix += char

        return prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix



