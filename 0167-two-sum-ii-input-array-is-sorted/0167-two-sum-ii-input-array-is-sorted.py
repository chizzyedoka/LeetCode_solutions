class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            if numbers[l] + numbers[r] < target:
                l+=1
            else:
                r-=1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # start, end = 0, len(numbers)-1
        # while start < end:
        #     initialSum = numbers[start] + numbers[end]
        #     if initialSum == target:
        #         return [start+1,end+1]
        #     elif initialSum > target:
        #         end -= 1
        #     else:
        #         start += 1