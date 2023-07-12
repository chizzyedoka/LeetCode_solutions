class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        # if len(haystack) == 1:
        #     return 0
        for i in range(len(haystack)-len(needle)+1):
            print(haystack[i:len(needle)+i])
            if needle == haystack[i:len(needle)+i]:
                return i
        return -1
        