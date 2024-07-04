class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        new_nums = nums + nums
        res = [-1] * len(new_nums)
        stack = []
        for i in range(len(new_nums)):
            # monotonic decreasing stack
            while stack and new_nums[stack[-1]] < new_nums[i]:
                top_pos = stack.pop()
                res[top_pos] = new_nums[i]
            stack.append(i)
        # while stack and len(stack)>=2:
        #     top_pos = stack.pop()
        #     res[top_pos] = nums[stack[-1]]
        return res[:len(nums)]
        