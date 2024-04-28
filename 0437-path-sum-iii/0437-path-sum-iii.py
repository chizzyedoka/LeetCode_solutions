# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, targetSum, path):
            if not node:
                return 0
            path.append(node.val)
            path_count, path_sum = 0,0
            for i in range(len(path)-1,-1,-1):
                path_sum += path[i]
                if path_sum == targetSum:
                    path_count += 1
            path_count += dfs(node.left, targetSum, path)
            path_count += dfs(node.right, targetSum, path)
            path.pop()
            return path_count
        return dfs(root, targetSum, [])
        