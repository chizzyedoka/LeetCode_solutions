# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, cur_sum):
            if not root:
                return 0
            cur_sum = cur_sum*10 + root.val
            if not root.left and not root.right:
                return cur_sum
            left_sum = dfs(root.left, cur_sum)
            right_sum = dfs(root.right, cur_sum)
            return left_sum + right_sum
        return dfs(root, 0)
        