class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # triangle inequality theory 
        # a + b > c
        # a + c > b
        # b + c > a
        # [4, 2, 3, 4]
        # [2, 3, 4, 4]
        # 1. [2, 3, 4] 2. [2, 4, 4] 3. [3, 4, 4] 4. [2, 3, 4]
        def binary_search(arr, target):
            l, r = 0,  len(arr) - 1
            while l <= r:
                mid = (l+r) // 2
                if arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return r # return the last index where arr[index] < target

        ans = 0
        n = len(nums)
        nums.sort()
        for i in range(n-2):
            if nums[i] == 0:
                continue
            for j in range(i+1, n-1):
                target_sum = nums[i] + nums[j]
                k = binary_search(nums[j+1:], target_sum)
                ans = ans + k + 1
        return ans
                
