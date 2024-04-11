class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        count = 0
        intervals.sort()
        prevEnd = intervals[0][1]
        for [start,end] in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                count+=1
                prevEnd = min(end,prevEnd)
        return count
                