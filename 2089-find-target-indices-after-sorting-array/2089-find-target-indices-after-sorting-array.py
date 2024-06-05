class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        
        def find_first(nums, target):
            first_occurence = -1
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left + right)//2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid -1
                else:
                    first_occurence = mid
                    right = mid -1
            return first_occurence
        
        def find_last(nums, target):
            last_occurence = -1
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left + right)//2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid -1
                else:
                    last_occurence = mid
                    left = mid +1
            return last_occurence
        
        first, last = find_first(nums, target), find_last(nums, target)
        if first == -1:
            return []
        return [x for x in range(first, last+1)]