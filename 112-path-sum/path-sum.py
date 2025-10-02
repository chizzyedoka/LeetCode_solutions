# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, target):
            if not node:
                return False
            if (not node.left) and (not node.right) and node.val == target:
                return True
            left = dfs(node.left, target-node.val)
            right = dfs(node.right, target-node.val)
            return left or right
        if not root:
            return False
        return dfs(root, targetSum)