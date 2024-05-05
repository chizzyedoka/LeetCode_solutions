class Solution:
    def reorganizeString(self, s: str) -> str:
        hashMap = {}
        maxHeap = []
        res = ""
        for char in s:
            if char not in hashMap:
                hashMap[char] = 0
            hashMap[char] += 1
        for key in hashMap.keys():
            heapq.heappush(maxHeap,(-hashMap[key], key))
        prev_char, prev_freq = None, 0
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            if prev_char and -prev_freq >0:
                heapq.heappush(maxHeap,(prev_freq,prev_char))
            res += char
            prev_char = char
            prev_freq = freq + 1
        return res if len(s)==len(res) else ""
        
        
        
#         import heapq
#         letterCounter = {}
#         maxHeap = []
        
#         for letter in s:
#             if letter not in letterCounter.keys():
#                 letterCounter[letter] = 0
#             letterCounter[letter] += 1
            
#         for k,v in letterCounter.items():
#             heapq.heappush(maxHeap,[-v,k])
        
#         previous = None
#         result = ""
        
#         while len(maxHeap) > 0:
#             count, letter = heapq.heappop(maxHeap)
#             result += letter
#             count += 1
                
#             if previous:
#                 heapq.heappush(maxHeap,previous)
#                 previous = None
                
#             if count != 0:
#                 previous = [count,letter]
        
#             if count != 0 and len(maxHeap) == 0:
#                 return ""
            
#         return result
                