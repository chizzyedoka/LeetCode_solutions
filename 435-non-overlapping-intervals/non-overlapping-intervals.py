class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        count = 0

        intervals.sort(key=lambda x: x[1]) # sort by endtimes
        prev_start, prev_end = intervals[0]

        for (start, end) in intervals[1:]:
            if start < prev_end: # there's an interval
                count += 1
            else:
                prev_end = end
        return count



