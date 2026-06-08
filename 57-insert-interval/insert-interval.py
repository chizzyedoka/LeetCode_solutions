class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def binary_search(arr, num):
            left, right = 0, len(arr) 
            while left < right:
                mid = (left + right) // 2
                if arr[mid] <= num:
                    left = mid + 1
                else:
                    right = mid
            return left

        if not intervals:
            return [newInterval]

        start_times = [interval[0] for interval in intervals]
        insert_index = binary_search(start_times, newInterval[0])
       
        intervals.insert(insert_index, newInterval)
        merged_intervals = []
        
        for (start, end) in intervals:
            if not merged_intervals:
                merged_intervals.append([start, end])
            else:
                prev_start, prev_end = merged_intervals[-1]

                if prev_end >= start:
                    merged_intervals[-1][1] = max(prev_end, end)
                else:
                    merged_intervals.append([start, end])
        return merged_intervals
        