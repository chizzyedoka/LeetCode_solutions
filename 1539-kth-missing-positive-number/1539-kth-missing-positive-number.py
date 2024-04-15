class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing =[]
        n =  len(missing)
        arr_set = set(arr)
        for i in range(len(arr)+k):
            if i+1 not in arr_set:
                missing.append(i+1)
                n += 1
            if n == k:
                break
            
        return missing[k-1]
            