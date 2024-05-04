class Solution:
    def frequencySort(self, s: str) -> str:
        hashMap = {}
        maxHeap = []
        res = ""
        for char in s:
            if char not in hashMap:
                hashMap[char] = 0
            hashMap[char] += 1
        for key in hashMap.keys():
            heapq.heappush(maxHeap,(-hashMap[key], key))
        while len(maxHeap) > 0:
            freq, char = heapq.heappop(maxHeap)
            substring = char * (-1*freq)
            res += substring
        return res