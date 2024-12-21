class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # get the number of zeros
        numZeros = 0
        for num in arr:
            if num == 0:
                numZeros += 1
                
        n = len(arr)
        i = n - 1 # pointer to the actual array
        j = n + numZeros - 1 # pointer to the extra space array
        
        while i >= 0:
            if j < n:
                arr[j] = arr[i]
                
            if arr[i] == 0:
                j -= 1
                if j < n:
                    arr[j] = 0
            j -= 1
            i -= 1