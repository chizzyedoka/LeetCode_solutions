class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        window_sum = sum(arr[:k])
        window_avg = window_sum / k
        if window_avg >= threshold:
            count += 1
        
        for window_end in range(k, len(arr)):
            window_sum += arr[window_end] - arr[window_end-k]
            window_avg = window_sum / k
            if window_avg >= threshold:
                count += 1
        return count