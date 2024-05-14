# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(node,hashmap):
            if not node:
                return False
            complement = k-node.val
            if complement in hashmap:
                return True
            hashmap[node.val]=True
            return dfs(node.left,hashmap) or dfs(node.right,hashmap)
        hashmap = {}
        return dfs(root,hashmap)
            