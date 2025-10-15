# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        root_to_leaf = []
        result = []
        def dfs(node):
            if not node:
                return

            root_to_leaf.append(chr(ord('a') + node.val))
            if not node.left and not node.right:
                result.append(root_to_leaf.copy())   

            dfs(node.left)
            dfs(node.right)
            root_to_leaf.pop()

        dfs(root)
        new_result = ["".join(leaf[::-1]) for leaf in result]
        new_result.sort()
        return new_result[0]

        
        