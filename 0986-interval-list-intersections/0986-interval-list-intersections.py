class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0,0
        res = []
        while i < len(firstList) and j < len(secondList):
            s1 = firstList[i][0]
            e1 = firstList[i][1]
            s2 = secondList[j][0]
            e2 = secondList[j][1]
            if (s2 >= s1 and s2 <= e1) or (s1 >= s2 and s1 <= e2 ):
                res.append([max(s1, s2),  min(e1, e2)])
            if e1 < e2:
                i += 1
            else:
                j += 1
        return res
            