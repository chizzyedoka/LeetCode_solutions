# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            counter +=1
            if counter == k:
                return cur.val
            cur = cur.right
        
        # def dfs(root):
        #     if not root:
        #         return
        #     dfs(root.left)
        #     output.append(root.val)
        #     dfs(root.right)
        # dfs(root)
        # return output[k-1]