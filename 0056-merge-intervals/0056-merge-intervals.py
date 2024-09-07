class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         if len(intervals) < 2:
#             return intervals
        
#         intervals.sort(key=lambda x: x[0])
#         output = [intervals[0]]
#         for start,end in intervals[1:]:
#             lastEnd = output[-1][1]
#             if start <= lastEnd:
#                 output[-1][1] = max(lastEnd,end)
#             else:
#                 output.append([start,end])
#         return output
    def merge(self,intervals):
        intervals.sort(key=lambda x: x[0])

        res = []
        prev_start, prev_end = intervals[0]

        for i in range(1, len(intervals)):
            start, end = intervals[i]


            if start <= prev_end:
                prev_end = max(prev_end, end)
            else:
                res.append([prev_start, prev_end])
                prev_start, prev_end = start, end


        res.append([prev_start, prev_end])

        return res