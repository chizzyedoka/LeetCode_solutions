class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j = 1,1
        # for i in range(1,len(nums)):
        while i < len(nums):
            if nums[i] != nums[j-1]:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j
        
        

        
        
        # i,j = 1, 1
        # while i < len(nums):
        #     if nums[j-1] != nums[i]:
        #         nums[j] = nums[i]
        #         j+=1
        #     i += 1
     
            
                
            