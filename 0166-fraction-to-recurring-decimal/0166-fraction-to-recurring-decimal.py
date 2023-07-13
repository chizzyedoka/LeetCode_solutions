class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        result = ""
        hashMap = {}
        if numerator == 0:
            return "0"
        
        if numerator * denominator < 0:
            result += '-'
            
        numerator = abs(numerator)
        denominator = abs(denominator)
        rem = numerator % denominator
        
        if rem == 0:
            result += str(numerator//denominator)
            return result
        
        result += str(numerator//denominator)
        result += '.'
        while rem > 0:
            if rem in hashMap:
                result = result[:hashMap[rem]] + "(" + result[hashMap[rem]:] + ")"
                break
            hashMap[rem] = len(result)
            numerator = rem *  10
            result += str(numerator//denominator)
            rem = numerator % denominator
        return result
            
            
        