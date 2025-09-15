class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            new_sum = numbers[l] + numbers[r]
            if new_sum > target:
                r -= 1
            elif new_sum < target:
                l += 1
            else:
                return [l+1, r+1]
                