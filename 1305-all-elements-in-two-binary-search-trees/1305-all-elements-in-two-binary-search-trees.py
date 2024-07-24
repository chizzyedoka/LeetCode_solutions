# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        tree_list = []
        def inorder(node):
            if not node:
                return
            tree_list.append(node.val)
            inorder(node.left)
            inorder(node.right)
        inorder(root1)
        inorder(root2)
        tree_list.sort()
        return tree_list
            
        