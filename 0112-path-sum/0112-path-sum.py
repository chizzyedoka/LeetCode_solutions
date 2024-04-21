# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
            if not root:
                return False
            stack = [root]
            sum_stack = [root.val]
            _sum = 0
            while stack:
                node = stack.pop()
                _sum = sum_stack.pop()
                if _sum == targetSum and not node.right and not node.left:
                    return True
                if node.right:
                    stack.append(node.right)
                    sum_stack.append(node.right.val + _sum)
                if node.left:
                    stack.append(node.left)
                    sum_stack.append(node.left.val + _sum)
            return False
            
            
            
            
            
            
            
#             if not root:
#                 return False
#             if targetSum == root.val and not root.left and not root.right:
#                 return True
#             return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    #     def dfs(node,curSum):
    #         if not node:
    #             return False
    #         curSum += node.val
    #         if not node.left and not node.right:
    #             if curSum == targetSum:
    #                 return True
    #         return (dfs(node.left,curSum)) or (dfs(node.right,curSum))
    #     return dfs(root,0)

#         if not root:
#             return False
#         if root.val == targetSum and root.left is None and root.right is None:
#             return True
#         return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)