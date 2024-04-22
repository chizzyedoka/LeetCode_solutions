# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # iterative solution
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return
#         stack = [root]
#         res = []
#         while stack:
#             root = stack.pop()
#             res.append(root.val)
#             if root.right:
#                 stack.append(root.right)
#             if root.left:
#                 stack.append(root.left)
#         return res

    # recursive solution--> passing the result
    # def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     res = []
    #     def preorder(root, res):
    #         if not root:
    #             return
    #         res.append(root.val)
    #         preorder(root.left,res)
    #         preorder(root.right,res)
    #     preorder(root,res)
    #     return res
    
    # recursive solution ii
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        


            
            
            