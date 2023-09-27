# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        nodeStack = []
        current = root
        while nodeStack or current:
            if current:
                nodeStack.append(current)
                current = current.left
            else:
                current = nodeStack.pop()
                result.append(current.val)
                current = current.right
        return result
#         if root:
#             return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
#         return []
        