class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip() # removes any white spaces
        s = s.split() # converts the input string to a list
        r = []
        for i in range(1,len(s)+1):
            r.append(s[len(s)-i] )
        return " ".join(r)
        