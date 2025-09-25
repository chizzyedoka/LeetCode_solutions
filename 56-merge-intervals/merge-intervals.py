class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        if not intervals:
            return []
        intervals.sort()
        for (start, end) in intervals:
            if not merged:
                merged.append([start, end])
            else:
                prev_start, prev_end = merged[-1]
                if prev_end >= start:
                    merged[-1][1] = max(end, prev_end)
                else:
                    merged.append([start, end])
        return merged
