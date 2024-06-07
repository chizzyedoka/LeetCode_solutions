# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def mountain_peak(arr: 'MountainArray',left, right):
            while left < right:
                mid = (left + right) // 2
                if arr.get(mid) > arr.get(mid+1):
                    right = mid
                else:
                    left = mid + 1
            return left
        
        def bin_search_asc(arr:'MountainArray', target,left, right):
            while left <= right:
                mid = (left+right)//2
                if arr.get(mid) < target:
                    left = mid + 1
                elif arr.get(mid) > target:
                    right = mid - 1
                else:
                    return mid
            return -1
        
        def bin_search_desc(arr: 'MountainArray', target, left, right):
            while left <= right:
                mid = (left + right) // 2
                mid_val = arr.get(mid)
                if mid_val > target:
                    left = mid + 1
                elif mid_val < target:
                    right = mid - 1
                else:
                    return mid
            return -1
        
        peak_index = mountain_peak(mountain_arr, 0, mountain_arr.length()-1)
        if mountain_arr.get(peak_index) == target:
            return peak_index
        found = bin_search_asc(mountain_arr,target,0,peak_index)
        if found == -1:
            found= bin_search_desc(mountain_arr,target, peak_index+1,mountain_arr.length()-1)
        return found
        