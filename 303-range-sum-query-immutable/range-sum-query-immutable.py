class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.prefix_sum_list = [0] * (n + 1)
        cur_sum = 0
        for i in range(1,n+1):
            self.prefix_sum_list[i] = self.prefix_sum_list[i-1] + nums[i-1]
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum_list[right+1] - self.prefix_sum_list[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)