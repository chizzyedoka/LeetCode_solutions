# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(root, path):
            if not root:
                return
            path.append(str(root.val))
            if not root.left and not root.right:
                res.append("->".join(path))
        
            if root.left:
                dfs(root.left, path)
            if root.right:
                dfs(root.right, path)
            path.pop()
            
        dfs(root, [])
        return res