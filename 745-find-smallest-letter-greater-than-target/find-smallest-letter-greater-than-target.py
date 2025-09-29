class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start, end = 0, len(letters)-1
        while start <= end:
            middle = (start + end)//2
            if letters[middle] > target:
                end = middle -1
            else:
                start = middle + 1
        if start == len(letters):
            return letters[0]
        return letters[start]
