class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row = [1] * numRows
        if numRows == 1:
            return [[1]]
        res = self.generate(numRows-1)
        prev_row = res[-1]
        for i in range(1,len(row)-1):
            row[i] = prev_row[i-1] + prev_row[i]
        res.append(row)
        return res
        