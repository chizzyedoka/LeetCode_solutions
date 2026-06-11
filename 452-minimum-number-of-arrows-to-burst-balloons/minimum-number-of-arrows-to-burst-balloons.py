class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        intervals = []
        points.sort()
        for (start, end) in points:
            if not intervals:
                intervals.append((start, end))
            prev_start, prev_end = intervals[-1]
            if start <= prev_end:
                intervals[-1] = max(prev_start, start), min(prev_end, end)
            else:
                intervals.append((start, end))

        return len(intervals)
