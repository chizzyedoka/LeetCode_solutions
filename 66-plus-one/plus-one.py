class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry =0

        for i in range(n-1, -1, -1):
            cur_index = n-i-1
            last_element = digits[cur_index] 

            cur_sum = last_element + 1 + carry

            digits[cur_index] = cur_sum // 10
            carry = cur_sum %10
        
        return digits

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        carry = 0
        n = len(digits)
        for i in range(n-1, -1, -1):
            lastElement = digits[i]
            if i == n-1:
                newLast = lastElement + 1 + carry
            else:
                newLast = lastElement + carry
            remainder = newLast % 10
            carry = newLast // 10
            result.append(remainder)
        if carry != 0:
            result.append(carry)
        return result[::-1]
