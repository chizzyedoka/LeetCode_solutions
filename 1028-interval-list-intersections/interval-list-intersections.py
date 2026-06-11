class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []

        if not firstList or not secondList:
            return result

        p1 = p2 = 0

        while p1 < len(firstList) and p2 < len(secondList):
            start1, end1 = firstList[p1]
            start2, end2 = secondList[p2]

            # move pointers when no intersection
            # 0 4
            # 6 8
            if start2 > end1:
                p1 += 1
            elif start1 > end2:
                p2 += 1
            else: # there's an intersection
                # 1 5  7 8
                # 2 7  8 10
                # 2 5 
                result.append([max(start1, start2), min(end1, end2)])
                if end1 < end2:
                    p1 += 1
                else:
                    p2 += 1
        return result
