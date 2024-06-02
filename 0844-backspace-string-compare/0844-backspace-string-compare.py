class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def newS(s):
            mys = []
            for i in range(len(s)):
                if s[i] != '#':
                    mys.append(s[i])
                else:
                    if len(mys)>0:
                        mys.pop()
            return mys
        news = newS(s)
        newt = newS(t)
        print(news, newt)
        return news == newt