class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # next smaller --> monotonic increasing
        stack = []
        res = prices
        for i in range(len(prices)):
            p = prices[i]
            while stack and prices[stack[-1]] >= p:
                pos = stack.pop()
                res[pos] = prices[pos] - p
            stack.append(i)
        return res