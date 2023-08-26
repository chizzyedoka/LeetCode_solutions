class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        hashMap = {}
        result = []
        if len(nums) == k:
            return nums
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 0
            hashMap[nums[i]] += 1
        # for keys,v in hashMap.items():
        #     if v >= k:
        #         result.append(keys)
        return heapq.nlargest(k, hashMap.keys(), key=hashMap.get) 
        
            
            