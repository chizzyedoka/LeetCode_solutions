# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
        
class Solution:
    
    # search for duplicate numbers
    def numIdenticalPairs(self, nums: List[int]) -> int:
        total_count = 0
        nums_counts = Counter(nums)
        print(nums_counts)
        for n,c in nums_counts.items():
            total_count += (c * (c-1)) //2
        return total_count

        