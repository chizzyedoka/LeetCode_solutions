class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        j = n
        res = []
        for _ in range(n):
            res.append(nums[i])
            res.append(nums[j])
            i += 1
            j += 1
        return res
            
        