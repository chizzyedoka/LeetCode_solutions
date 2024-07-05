
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack, discount, l =[], [0]*len(prices), len(prices)

        for i in range(l):
            while stack and prices[i] <= prices[stack[-1]]:
                discount[stack.pop()] = prices[i]
            stack.append(i)
        ans = []
        for i in range(l):
            ans.append(prices[i]-discount[i])
        
        return ans