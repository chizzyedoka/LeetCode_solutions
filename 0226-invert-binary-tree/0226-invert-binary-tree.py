# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if not root:
#             return
#         q = deque([root])
#         while q:
#             size = len(q)
#             node = q.popleft()
#             node.left, node.right = node.right, node.left
#             for _ in range(size):
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#         return root
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        q = deque([root])
        while q:
            node = q.popleft()
            
            # Swap the left and right children
            node.left, node.right = node.right, node.left
            
            # Add the children to the queue if they are not None
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return root
