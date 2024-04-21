# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        stack = [root]
        res = []
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return res
            
        
       
        
        
        
        
#         if not root:
#             return []
#         result = []
#         stack = [root]
#         while stack:
#             node = stack.pop()
#             result.append(node.val)
#             if node.right:
#                 stack.append(node.right)
#             if node.left:
#                 stack.append(node.left)
#         return result
#         if root == None:
#             return []
#         return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
                 

            
            
            