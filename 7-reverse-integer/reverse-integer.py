class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1
        is_negative = x < 0
        x =abs(x)
        new_x = 0
        while x:
            last_digit = x % 10
            x = x // 10
            new_x = new_x*10 + last_digit
            if new_x > MAX_INT:
                return 0
        return -1*new_x if is_negative else new_x