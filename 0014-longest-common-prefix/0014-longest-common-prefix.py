class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        
        min_len = min([len(x) for x in strs])
        if min_len == 0:
            return ''
        
        result = []
        for idx in range(min_len):
            c = ''
            for str in strs:
                if len(c) == 0:
                    c = str[idx]
                elif str[idx] != c:
                    return strs[0][:idx]
        return strs[0][:idx+1]