class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        if target >=letters[n-1]:
            return letters[0]
        
        start, end = 0, n-1
        while start <= end:
            mid = (start + end)// 2
            if letters[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
        return letters[start%n]
        