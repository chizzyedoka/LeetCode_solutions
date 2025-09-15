class Solution:
    def reverse(self, x: int) -> int:
        # 123 % 10 = 3
        # 123 // 10 = 12

        # 12 % 10 = 2
        # 12 // 10 = 1
        is_neg = x < 0
        x = abs(x)
        x_reversed = 0
        MAX_INT = 2**31

        while x:
            digit = x % 10
            x = int(x // 10)
            x_reversed = (x_reversed*10) + digit
            if x_reversed > MAX_INT:
                return 0

        if is_neg:
            return -1*x_reversed
        return x_reversed

