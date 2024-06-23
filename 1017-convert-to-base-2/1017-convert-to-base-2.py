class Solution:
    def baseNeg2(self, n: int) -> str:
        stack = []
        if n == 0:
            return "0"
        
        while n != 0:
            r = n % -2
            n = n // -2
            if r < 0:
                r += 2
                n += 1
            stack.append(str(r))
        res = ""
        while stack:
            res += stack.pop()
        return res
        
        