class Solution:
    def reorganizeString(self, s: str) -> str:
        import heapq
        letterCounter = {}
        maxHeap = []
        
        for letter in s:
            if letter not in letterCounter.keys():
                letterCounter[letter] = 0
            letterCounter[letter] += 1
            
        for k,v in letterCounter.items():
            heapq.heappush(maxHeap,[-v,k])
        
        previous = None
        result = ""
        
        while len(maxHeap) > 0:
            count, letter = heapq.heappop(maxHeap)
            result += letter
            count += 1
                
            if previous:
                heapq.heappush(maxHeap,previous)
                previous = None
                
            if count != 0:
                previous = [count,letter]
        
            if count != 0 and len(maxHeap) == 0:
                return ""
            
        return result
                