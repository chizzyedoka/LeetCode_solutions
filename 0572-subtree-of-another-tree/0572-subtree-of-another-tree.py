# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        def isSameTree(s: TreeNode, t: TreeNode) -> bool:
            if not s and not t:
                return True
            if not s or not t:
                return False
            return s.val == t.val and isSameTree(s.left, t.left) and isSameTree(s.right, t.right)
        
        def dfs(node: TreeNode) -> bool:
            if not node:
                return False
            if isSameTree(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)