class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
            res = []
            last_term = digits[-1] + 1 # add 1 to the last digit
            carry_over = last_term // 10
            res.append(last_term%10)
            i = len(digits) - 2
            while i >= 0:
                temp = carry_over + digits[i]
                carry_over = temp//10
                res.append(temp%10)
                i -= 1
        
            if carry_over > 0:
                res.append(1)
                return res[::-1]
            return res[::-1]
        