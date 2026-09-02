class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # map, cause we need the index
        # for each element, check if the element's  compliment exits in the set
        # if it does return their indexes
        # else store in the set the element and its index
        hashmap = {}
        for i in range(len(nums)):
            num = nums[i]
            compliment = target - num
            if compliment in hashmap:
                return [i, hashmap[compliment]]
            hashmap[num] = i