class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()

        merged_intervals = [intervals[0]]

        for (start, end) in intervals[1:]:
            prev_start, prev_end = merged_intervals[-1]

            if prev_end >= start:
                merged_intervals[-1] = [prev_start, max(prev_end, end)]
            else:
                merged_intervals.append([start, end])
        
        return merged_intervals