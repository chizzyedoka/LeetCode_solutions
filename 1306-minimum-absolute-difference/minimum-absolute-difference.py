class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        if not arr:
            return []
        result = []
        MIN_DIFF = float("inf")
        arr.sort()
        n = len(arr)

        for i in range(1,n):
            a = arr[i-1]
            b = arr[i]
            diff = b - a
            MIN_DIFF = min(MIN_DIFF, diff)

        for i in range(1,n):
            a = arr[i-1]
            b = arr[i]
            diff = b - a
            if diff == MIN_DIFF:
                result.append((a,b))

        return result
