class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        average = 0
        window_sum = 0
        #for i in range(len(arr)-k+1):
        for i in range(len(arr)):
            window_sum += arr[i]
            if i >= k:
                window_sum -= arr[i-k]
            if  i >= k - 1 and window_sum // k >= threshold:
                count += 1
        return count
        #     window = arr[i:i+k]
        #     window_sum = sum(window)
        #     average = window_sum//k
        #     if average >= threshold:
        #         count+= 1
        # return count

#     def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
#         ans = 0
#         windowSum = 0

#         for i in range(len(arr)):
#         windowSum += arr[i]
#         if i >= k:
#             windowSum -= arr[i - k]
#         if i >= k - 1 and windowSum // k >= threshold:
#             ans += 1

#     return ans
        
        