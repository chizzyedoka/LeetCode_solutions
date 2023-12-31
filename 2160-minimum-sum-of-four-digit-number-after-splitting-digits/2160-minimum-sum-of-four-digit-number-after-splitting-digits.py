class Solution:
    def minimumSum(self, num: int) -> int:
        num_str = str(num)
        num_list = list(num_str)
        num_list.sort()
        first_min = num_list[0]
        second_min = num_list[1]
        new1 = first_min + num_list[2]
        new2 = second_min + num_list[3]
        return int(new1) + int(new2)
        
            
            
        