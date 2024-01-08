# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
        
# class Solution:
    
    # search for duplicate numbers
#def numIdenticalPairs(self, nums: List[int]) -> int:
        # total_count = 0
        # nums_counts = Counter(nums)
        # for n,c in nums_counts.items():
        #     total_count += (c * (c-1)) //2
        # return total_count

class Solution:
    def numIdenticalPairs(self, nums):
        # Brute force
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             count += 1
        # return count

        # Slightly optimized
        total_count = 0
        same_count = 0
        curr_num = float('-inf')
        nums.sort()

        for num in nums:
            if curr_num != num:
                curr_num = num
                same_count = 0
            else:
                total_count += same_count + 1
                same_count += 1

        return total_count

# Example usage:
# solution = Solution()
# nums = [1, 2, 3, 1, 2, 3, 1, 1, 2]
# result = solution.numIdenticalPairs(nums)
# print(result)
