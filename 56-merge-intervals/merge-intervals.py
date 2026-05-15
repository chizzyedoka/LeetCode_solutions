class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals

        intervals.sort()
        result = [ [intervals[0][0], intervals[0][1] ]]

        for (start, end) in intervals[1:]:
            prev_start, prev_end = result[-1]

            if prev_end >= start:
                result[-1][1] = max(end, prev_end)
            else:
                result.append([start, end])
        return result

