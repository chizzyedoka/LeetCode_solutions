class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        # does multipliers have to be sorted? and why?
        # no, because from the question we were told the order matters => add multipliers[i]
       
        
        # we need 3 states (can be reduced to 2) i, left, right -> i is the current operation, left is positiom
        # of in nums from the start side, right is the position from the end side
        
        # dp(i, left, right) -> returns the maximum score we can accumulate from operation i, and remaining availaible numbers in nums
        # that span from left to right
        # for nums = [1,2,3], multipliers = [3,2,1] the starting state is dp(0, 0, 2) and the final state is dp(2, 0, 0)

        # RECURRENCE 
        # max( mult[i] * nums[left] + dp(i+1, left+1, right), 
        #      mult[i] * nums[right] + dp(i+1,left, right-1)  )

        # base case
        # when we have nothing left to choose from i == len(multipliers)

        n = len(nums)
        m = len(multipliers)
        mult = multipliers

        memo = {}

        def dp(i, left, right):
            if i == m:
                return 0
            if (i, left, right) not in memo:
                memo[(i,left,right)] = max( mult[i] * nums[left] + dp(i+1, left+1, right), 
                                            mult[i] * nums[right] + dp(i+1,left, right-1)  )
            return memo[(i, left, right)]

        return dp(0,0,n-1)

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        n = len(nums)
        m = len(multipliers)
        mult = multipliers

        memo = {}
        # right = n - 1 - (i - left)

        def dp(i, left):
            if i == m:
                return 0
            if (i, left) not in memo:
                memo[(i,left)] = max( mult[i] * nums[left] + dp(i+1, left+1), 
                                            mult[i] * nums[n-1-(i-left)] + dp(i+1, left)  )
                                            
            return memo[(i, left)]

        return dp(0,0,)
        
