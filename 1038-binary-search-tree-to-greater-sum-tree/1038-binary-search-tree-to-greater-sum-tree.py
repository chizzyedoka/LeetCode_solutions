# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node, tree_lst):
            if not node:
                return
            dfs(node.left, tree_lst)
            tree_lst.append(node.val)
            dfs(node.right, tree_lst)
        
        def replace_values(node):
            if not node:
                return
            replace_values(node.left)
            replace_values(node.right)
            node_sum = 0
            for i in tree_lst:
                if i > node.val:
                    node_sum += i
                else:
                    break
            node.val += node_sum
            
        tree_lst = []
        dfs(root, tree_lst)
        tree_lst.reverse()
        replace_values(root)
        return root
        
        
            
        