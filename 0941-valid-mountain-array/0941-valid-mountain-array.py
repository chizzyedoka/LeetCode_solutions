class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        declineIndex = None
        # get increasing part
        for i in range(1,len(arr)):
            if arr[i] < arr[i-1]:
                declineIndex = i
                break
            if arr[i] == arr[i-1]:
                return False
        if not declineIndex or declineIndex ==1 :
            return False
        print(declineIndex)
        for i in range(declineIndex,len(arr)-1):
            if arr[i+1] > arr[i]:
                return False
            if arr[i] == arr[i-1]:
                return False
        return True