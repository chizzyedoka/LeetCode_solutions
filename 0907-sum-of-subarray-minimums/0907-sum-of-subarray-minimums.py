class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        M = 10**9+7
        sums = 0
        arr.append(0) #Sentinel value to pop all elements off the stack
        stack = [-1]
        
        for i2,num in enumerate(arr):
	      #Mantain a monotone increasing stack
            while stack and num < arr[stack[-1]]:
                index = stack.pop()
                i1 = stack[-1]   # First lesser element to the left
                left = index-stack[-1]
                right = i2-index
                sums += right*left*arr[index]
            stack.append(i2)
        return sums%M
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

        # # get all subsets
        # subsets = []
        # subsets.append([])
        # for num in arr:
        #     n = len(subsets)
        #     for i in range(n):
        #         set = list(subsets[i])
        #         set.append(num)
        #         subsets.append(set)
        # # get sum of minimum in eachsubsets
        # totalMin = 0
        # for sub in subsets:
        #     if len(sub) > 0:
        #         totalMin += min(sub)
        # print(subsets)
        # return totalMin
        