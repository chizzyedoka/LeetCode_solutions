class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        windowSum = sum(arr[:k])
        if windowSum / k >= threshold:
            count += 1
            
        for i in range(len(arr)-k):
            windowSum += -1* arr[i] + arr[i+k]
            if windowSum/k >= threshold:
                count += 1
        
        return count
      
        