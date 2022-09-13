class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num_int = 0
        for i in num:
            num_int =  (num_int*10) + i
        temp = str(num_int + k)
        output = [j for j in temp]
        return output