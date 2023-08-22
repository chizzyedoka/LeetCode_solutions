class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        d = len(s)
        s= list(s)
        while d>0:
            temp = s[0]
            s.pop(0)
            s.append(temp)
            if "".join(s) ==goal:
                return True
            d-=1
        return False  
        