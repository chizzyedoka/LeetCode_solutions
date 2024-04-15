class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing =[]
        arr_set = set(arr)
        for i in range(len(arr)+k):
            if i+1 not in arr:
                missing.append(i+1)
        print(missing)
        return missing[k-1]
            