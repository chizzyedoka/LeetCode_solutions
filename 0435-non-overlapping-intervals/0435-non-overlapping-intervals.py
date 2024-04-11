class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        count = 0
        s1,e1 = intervals[0][0], intervals[0][1]
        for i in range(1,len(intervals)):
            s2, e2 = intervals[i][0], intervals[i][1]
            if e1 > s2: # overlapping
                count += 1
                e1 = min(e1,e2)
            else:
                s1,e1 = s2, e2
        return count