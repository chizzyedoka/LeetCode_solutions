class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # exchange values if num1 is lengthier
        if len(num1) > len(num2): # num2 should always be lengthier than num1
            num3, num1 = num1, num2
            num2 = num3
        out = []
        carry_over = 0
        i = len(num2) - 1
        j = len(num1) - 1
        
        while i >= 0:
            if j < 0: # no more values in num1
                temp = int(num2[i]) + carry_over
                out.append(str(temp%10))
                carry_over = temp // 10
                if i == 0 and carry_over > 0:
                    out.append(str(carry_over))
                
            else:
                temp = int(num2[i]) + int(num1[j]) + carry_over
                remainder = temp % 10
                carry_over = temp // 10
                out.append(str(remainder))
                
                if i == 0 and carry_over > 0:
                    out.append(str(carry_over))
            i -=1
            j -= 1
        return "".join(out[::-1])