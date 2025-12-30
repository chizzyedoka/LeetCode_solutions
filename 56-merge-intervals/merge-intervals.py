class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_intervals = [intervals[0]]

        for [start, end] in intervals[1:]:
            prev_start, prev_end = merged_intervals[-1]

            if prev_end >= start:
                merged_intervals.pop()
                merged_intervals.append((prev_start,max(end, prev_end)))
            
            else:
                merged_intervals.append((start, end))

        return merged_intervals

