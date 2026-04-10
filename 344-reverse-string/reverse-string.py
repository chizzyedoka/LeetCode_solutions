class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        leftPointer, rightPointer = 0, len(s)-1

        while leftPointer < rightPointer:
            s[leftPointer], s[rightPointer] = s[rightPointer], s[leftPointer]
            leftPointer += 1
            rightPointer -= 1
        