class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)
            cur_sum = 0
            for digit in str(n):
                cur_sum += int(digit)**2
            n = cur_sum

        return True