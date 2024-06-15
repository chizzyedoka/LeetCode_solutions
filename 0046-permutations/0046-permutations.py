class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(tempList: List[int]):
            if len(tempList) == len(nums):
                res.append(tempList[:])
            else:
                for num in nums:
                    if num in tempList:
                        continue
                    tempList.append(num)
                    backtrack(tempList)
                    tempList.pop()
        
        res = []
        backtrack([])
        return res


