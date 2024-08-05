class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            max_jump = nums[i]
            if i + max_jump >= goal:
                goal = i
        return goal == 0