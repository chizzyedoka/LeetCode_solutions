# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        values = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)
        dfs(root)
        dummy = TreeNode(0)
        cur = dummy
        for val in values:
            cur.right = TreeNode(val)
            cur = cur.right
        return dummy.right