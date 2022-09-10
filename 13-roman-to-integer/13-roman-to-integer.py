class Solution:
    def romanToInt(self, s: str) -> int:
        # create dictionary of base roman numerals
        H = {'I':1, 'V': 5, 'X': 10, 'L':50, 'C' : 100, 'D' : 500, 'M': 1000}
        total = 0
        prev = 0
        for i in range(len(s)):
            currentVal = H[s[i]]
            
            if i == len(s) -1:
                nextVal = 0
            else:
                nextVal = H[s[i+1]]
            if currentVal >= nextVal:
                total += currentVal
            
            else:
                total -= currentVal
        return total
        