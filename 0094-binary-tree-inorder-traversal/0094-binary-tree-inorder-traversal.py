# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        node = root
        result = []
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node= node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        