# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMax(node):
            curr = node
            while curr and curr.right: #largest node is all the way to the right
                curr = curr.right
            return curr       
        # base case
        if not root:
            return None
        # find the key root
        if key < root.val: # key is in left subtree
            root.left = self.deleteNode(root.left,key)
        elif key > root.val: # key is in right subtree
            root.right = self.deleteNode(root.right,key)
        else: # found key
            if not root.left: # no left subtree
                return root.right
            elif not root.right: # no right subtree
                return root.left
            else:
                # find the largest Node in the left tree
                maxNode = findMax(root.left)
                root.val = maxNode.val
                root.left = self.deleteNode(root.left, root.val)
        return root
            