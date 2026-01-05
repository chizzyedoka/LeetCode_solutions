class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        totalSum = 0
        numOfNeg = 0
        smallestAbsValue = float('inf')
        m, n = len(matrix), len(matrix[0])
        for r in range(m):
            for c in range(n):
                num = matrix[r][c]
                if num < 0:
                    numOfNeg += 1
                smallestAbsValue = min(smallestAbsValue, abs(num))
                totalSum += abs(num)

        if (numOfNeg % 2) == 0:
            return totalSum
        else:
            return totalSum - 2*smallestAbsValue 