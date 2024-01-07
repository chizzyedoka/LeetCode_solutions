# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
        
class Solution:
    
    # search for duplicate numbers
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        # number of good pairs
        repeat = {}
        num = 0
        
        # for every element in nums
        for v in nums:
            
            # number of repeated digits
            if v in repeat:
                
                # count number of pairs based on duplicate values
                if repeat[v] == 1:
                    num += 1
                else:
                    num += repeat[v]
                
                # increment the number of counts
                repeat[v] += 1
            # number has not been seen before
            else:
                repeat[v] = 1
        # return
        return num
        # initialize a count at 0
        # sort the array
        # loop through the array
        # compare the first element with the next
        # if the same increase the count by 1
        # continue this  until we get a different element
        # make the new element the next to compare
        # continue until you get to end of loop
#         count,total_count = 0,0
#         nums.sort()
#         cur_num = -1
#         for i in range(len(nums)):
#             if cur_num != nums[i]:
#                 cur_num = nums[i]
#                 count += 1
#             else:
#                 total_count += count + 1
#                 count += 1
            
#         return total_count
    
#     int total_count = 0;
#         int same_count = 0;
#         int curr_num = -1;
#         std::sort(nums.begin(),nums.end());
        
#         for(int i = 0 ; i < nums.size(); i++){
#             if(curr_num!=nums[i]){
#                 curr_num = nums[i];
#                 same_count = 0;
#             }else{
#                 total_count += same_count + 1;
#                 same_count += 1;
#             }
#         }
#         return total_count;

        