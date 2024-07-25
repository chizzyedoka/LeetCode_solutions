# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            lst.append(node.val)
            inorder(node.right)
        
        def arrange(lst):
            if not lst:
                return
            mid = len(lst)//2
            root = TreeNode(lst[mid])
            root.left = arrange(lst[:mid])
            root.right = arrange(lst[mid+1:])
            return root
        
        lst = []
        inorder(root)
        return arrange(lst)
        