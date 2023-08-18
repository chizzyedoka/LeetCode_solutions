class Solution:
    def isHappy(self, n: int) -> bool:
        def digit_sum(n):
            digit_sum = 0
            while n > 0:
                digit = n % 10
                n //= 10
                digit_sum += digit**2
            return digit_sum
        slow = n
        fast = digit_sum(n)
        while fast != 1 and slow != fast:
            slow = digit_sum(slow)
            fast = digit_sum(digit_sum(fast))
        return fast == 1
        # def digit_sum(n):
        #     digit_sum = 0
        #     while n > 0:
        #         digit = n % 10
        #         n //= 10
        #         digit_sum += digit**2
        #     return digit_sum
        # seen = set()
        # while n != 1:
        #     seen.add(n)
        #     n = digit_sum(n)
        #     if n in seen:
        #         return False
        # return True
        
    
        