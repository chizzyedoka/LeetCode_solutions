# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        output=[]
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            output.append(cur.val)
            cur = cur.right
        return output[k-1]
        # def dfs(root):
        #     if not root:
        #         return
        #     dfs(root.left)
        #     output.append(root.val)
        #     dfs(root.right)
        # dfs(root)
        # return output[k-1]