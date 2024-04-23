# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursive i
    #def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # def inorder(root):
        #     if not root:
        #         return []
        #     return inorder(root.left) + [root.val] + inorder(root.right)
        # return inorder(root)
      
    # recursive ii -> faster, passing the result
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(root,res):
            if not root:
                return 
            inorder(root.left,res)
            res.append(root.val)
            inorder(root.right,res)
        inorder(root,res)
        return res
    
    # iterative solution
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur=cur.right
        return res
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = []
#         stack = []
#         cur = root
#         while stack or cur:
#             while cur:
#                 stack.append(cur)
#                 cur = cur.left
#             cur = stack.pop()
#             res.append(cur.val)
#             cur = cur.right
#         return res
        
        
#         result = []
#         stack = []
#         cur = root
#         while stack or cur:
#             while cur:
#                 stack.append(cur)
#                 cur = cur.left
#             cur = stack.pop()
#             result.append(cur.val)
#             cur = cur.right
#         return result
        
        
        
        
        
        # result = []
        # nodeStack = []
        # current = root
        # while nodeStack or current:
        #     if current:
        #         nodeStack.append(current)
        #         current = current.left
        #     else:
        #         current = nodeStack.pop()
        #         result.append(current.val)
        #         current = current.right
        # return result
    
        # stack = []
        # result = []
        # curr = root
        # while stack or curr:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
        #     curr = stack.pop()
        #     result.append(curr.val)
        #     curr = curr.right
        # return result
        
#         if root:
#             return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
#         return []
        