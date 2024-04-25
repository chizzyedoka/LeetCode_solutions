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
        
        def dfs(node, current_sum):
            if not node:  # If the node is None, return False
                return False
            
            current_sum -= node.val  # Subtract the node's value from the current sum
            
            if not node.left and not node.right:  # Check if it's a leaf node
                return current_sum == 0  # If the current sum is 0, return True
            
            # Recur for left and right subtrees
            return dfs(node.left, current_sum) or dfs(node.right, current_sum)
        
        return dfs(root, targetSum)

    
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         def dfs(node, _sum):
#             if not node:
#                 return False
            
#             if not node.left and not node.right:
#                 return _sum == node.val
            
#             left_path = dfs(node.left, _sum - node.val)
#             right_path = dfs(node.right, _sum - node.val)
            
#             return left_path or right_path
        
#         if not root:
#             return False
        
#         return dfs(root, targetSum)
        
     # def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
     #        if not root:
     #            return False
     #        stack = [root]
     #        sum_stack = [root.val]
     #        while stack:
     #            node = stack.pop()
     #            _sum = sum_stack.pop()
     #            if _sum == targetSum and not node.right and not node.left:
     #                return True
     #            if node.right:
     #                stack.append(node.right)
     #                sum_stack.append(node.right.val + _sum)
     #            if node.left:
     #                stack.append(node.left)
     #                sum_stack.append(node.left.val + _sum)
     #        return False
            
            
            
            
            
            
            
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