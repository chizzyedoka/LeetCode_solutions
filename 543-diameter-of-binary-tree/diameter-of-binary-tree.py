# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def getLength(node):
            if not node:
                return 0
            left = getLength(node.left)
            right = getLength(node.right)
            self.diameter =  max(self.diameter, left + right)
            return 1 + max(left,right)
           

        if not root:
            return 0
        getLength(root)
        return self.diameter