# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        my_set = set()
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            my_set.add(node.val)
            dfs(node.right)
        dfs(root)
        if len(my_set) < 2:
            return -1
        my_list = sorted(my_set)
        return my_list[1]
        