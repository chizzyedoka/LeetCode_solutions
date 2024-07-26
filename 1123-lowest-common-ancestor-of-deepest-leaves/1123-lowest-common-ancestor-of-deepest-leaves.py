# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def lca_multiple_nodes(root, nodes):
            if not root or root in nodes:
                return root
            left = lca_multiple_nodes(root.left, nodes)
            right = lca_multiple_nodes(root.right, nodes)
            if left and right:
                return root
            elif left:
                return left
            return right
            
            
        if not root:
            return
        q = deque([root])
        deepest_leaves = []
        while q:
            size = len(q)
            level = []
            for _ in range(size):
                node = q.popleft()
                level.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            deepest_leaves = level
            
        return lca_multiple_nodes(root, deepest_leaves)
            