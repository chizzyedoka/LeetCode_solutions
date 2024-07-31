# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
#         path_count = 0
#         def dfs(node, curSum):
#             if not node:
#                 return
#             curSum += node.val
#             if curSum == targetSum:
#                 path_count += 1
#                 return
#             if curSum > targetSum:
#                 curSum -= node.val
#             dfs(node.left, curSum)
#             dfs(node.right, curSum)
#         dfs(root, 0)
#         return pathCount
                
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.path_count = 0

        def dfs(node, curSum):
            if not node:
                return
            curSum += node.val
            if curSum == targetSum:
                self.path_count += 1
            dfs(node.left, curSum)
            dfs(node.right, curSum)
        
        def traverse(node):
            if not node:
                return
            dfs(node, 0)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return self.path_count
