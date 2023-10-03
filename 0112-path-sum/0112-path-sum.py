# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    #     def dfs(node,curSum):
    #         if not node:
    #             return False
    #         curSum += node.val
    #         if not node.left and not node.right:
    #             if curSum == targetSum:
    #                 return True
    #         return (dfs(node.left,curSum)) or (dfs(node.right,curSum))
    #     return dfs(root,0)

        if not root:
            return False
        if root.val == targetSum and root.left is None and root.right is None:
            return True
        return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)