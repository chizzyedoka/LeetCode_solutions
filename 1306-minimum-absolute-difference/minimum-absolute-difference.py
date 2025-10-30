class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        if not arr:
            return []
        
        MIN_DIFF = float("inf")
        arr.sort()
        n = len(arr)
        diff_map = defaultdict(list)

        for i in range(1,n):
            a = arr[i-1]
            b = arr[i]
            diff = b - a
            MIN_DIFF = min(MIN_DIFF, diff)
            diff_map[diff].append((a,b))

        

        return diff_map[MIN_DIFF]
