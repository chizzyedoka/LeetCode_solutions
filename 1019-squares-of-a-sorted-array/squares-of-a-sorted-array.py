class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        leftPointer, rightPointer = 0, n-1
        currentPointer = n-1
        result = [0] * n

        while leftPointer <= rightPointer:
            leftSquared = nums[leftPointer] ** 2
            rightSquared = nums[rightPointer] ** 2
            if leftSquared > rightSquared:
                result[currentPointer] = leftSquared
                leftPointer +=1
            else: 
                result[currentPointer] = rightSquared
                rightPointer -=1
            currentPointer -= 1
        return result
