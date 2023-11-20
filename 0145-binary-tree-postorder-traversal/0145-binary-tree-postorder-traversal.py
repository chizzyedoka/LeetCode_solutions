# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

        
#         # recursive solution
#         # result = []
#         # def postorder(root):
#         #     if not root:
#         #         return
#         #     postorder(root.left)
#         #     postorder(root.right)
#         #     result.append(root.val)
#         # postorder(root)
#         # return result
        
#         # recursive solution
#         # if root: #root is not null
#         #     return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
#         # return []


class Solution(object):
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.insert(0,root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
                
        return output

            
            
        