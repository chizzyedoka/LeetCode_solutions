# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:    
        result = []
        if not root:
            return
        
        nodeStack = []
        nodeStack.append(root)
        while len(nodeStack) > 0:
            node = nodeStack.pop()
            result.append(node.val)
            
            if node.right:
                nodeStack.append(node.right)
            if node.left:
                nodeStack.append(node.left)
        return result
#         if root == None:
#             return []
#         return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
            
            
            
            