# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0,1

            left,lefti = dfs(node.left)
            right,righti = dfs(node.right)

            return max(left,right)+1,max(lefti,righti,left+right+1)

        return dfs(root)[1]-1
        