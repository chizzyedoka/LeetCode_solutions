# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max_node = float('-inf')
        self.amount = 0
        def dfs(node, max_node):
            if not node:
                return
            if node.val >= max_node:
                self.amount+=1
                max_node = node.val
            if node.left:
                dfs(node.left, max_node)
            if node.right:
                dfs(node.right, max_node)
        dfs(root, max_node)
        return self.amount