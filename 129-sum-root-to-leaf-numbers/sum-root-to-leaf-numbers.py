# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        def dfs(node, curSum):
            if not node:
                return 0
            curSum = curSum*10 + node.val
            if (not node.left) and (not node.right):
                self.total += curSum
            dfs(node.right, curSum)
            dfs(node.left, curSum)

        if not root:
            return 0
        dfs(root, 0)
        return self.total