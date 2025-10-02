# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node,curPath, curSum):
            if not node:
                return
            curSum += node.val
            curPath.append(node.val)
            if (not node.left) and (not node.right) and curSum == targetSum:
                result.append(curPath[:])
            
            left = dfs(node.left, curPath, curSum)
            right = dfs(node.right, curPath, curSum)
            curPath.pop()

        dfs(root, [], 0)
        return result
        