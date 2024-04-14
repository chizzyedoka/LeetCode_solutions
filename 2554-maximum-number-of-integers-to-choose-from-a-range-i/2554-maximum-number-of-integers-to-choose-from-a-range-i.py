class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        count = 0
        seen = set(banned)
        current_sum = 0
        for i in range(1, n+1):
            if i not in seen:
                current_sum += i
                if current_sum <= maxSum:
                    count += 1
        return count
