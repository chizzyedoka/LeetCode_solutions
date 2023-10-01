# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            result.append(root.val)
        postorder(root)
        return result
        
        # recursive solution
        # if root: #root is not null
        #     return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        # return []
    
            
            
        