class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        hashMap = {}
        res = []
        maxHeap = []
        
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 0
            hashMap[nums[i]] += 1
        
        for (key,v) in hashMap.items():
            heapq.heappush(maxHeap,(-v,key))
            
        print(hashMap,k)
        
        while k>0:
            res.append(heapq.heappop(maxHeap)[1])
            k-=1   
        return res
        
        
        
        # import heapq
        # hashMap = {}
        # result = []
        # if len(nums) == k:
        #     return nums
        # for i in range(len(nums)):
        #     if nums[i] not in hashMap:
        #         hashMap[nums[i]] = 0
        #     hashMap[nums[i]] += 1
        # values = list(hashMap.values())
        # heapq.heapify(values)
        # return heapq.nlargest(k, hashMap.keys(), key=hashMap.get) 
        
            
            