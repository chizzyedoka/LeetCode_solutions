class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        minHeap = []
        hashMap = {}
        for num in arr:
            if num not in hashMap:
                hashMap[num] = 0
            hashMap[num] += 1
        
        for key in hashMap.keys():
            heapq.heappush(minHeap,(hashMap[key],key))
            
        while k > 0:
            freq,val = heapq.heappop(minHeap)
            if freq >1:
                heapq.heappush(minHeap, (freq-1, val))
            k -= 1
        return len(minHeap)
