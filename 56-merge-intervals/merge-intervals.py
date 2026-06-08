class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_intervals = []

        if not intervals:
            return merged_intervals

        intervals.sort()

        for (start, end) in intervals:
            if not merged_intervals or (start > merged_intervals[-1][1]):
                merged_intervals.append([start, end])
            else:
                # change the prev end to max of the prev end and cur end
                merged_intervals[-1][1] = max(end, merged_intervals[-1][1])
        return merged_intervals
