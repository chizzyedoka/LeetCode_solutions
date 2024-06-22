class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        temps = temperatures
        n = len(temps)
        ans = [0] * n
        for i, t in enumerate(temps):
            while stack and t > stack[-1][1]:
                index, temp = stack.pop()
                ans[index] = i-index
            stack.append((i,t))
        return ans
            