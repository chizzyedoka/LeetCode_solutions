# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def findSum(node, curSum):
            if not node:
                return 0
            curSum += node.val
            if curSum == targetSum:
                count = 1
            else:
                count = 0
            count += findSum(node.left, curSum)
            count += findSum(node.right, curSum)
            return count

        if not root:
            return 0

        

        return findSum(root, 0) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)