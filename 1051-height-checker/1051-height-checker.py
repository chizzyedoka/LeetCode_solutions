class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heightsCopy = heights.copy()
        heights.sort()
        outOfOrder = 0
        for i in range(len(heights)):
            if heights[i] != heightsCopy[i]:
                outOfOrder += 1
        return outOfOrder
        