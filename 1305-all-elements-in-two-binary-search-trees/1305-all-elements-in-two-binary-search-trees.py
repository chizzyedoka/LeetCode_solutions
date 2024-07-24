# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(node,lst):
            if not node:
                return
            inorder(node.left, lst)
            lst.append(node.val)
            inorder(node.right, lst)
        lst1, lst2 = [], []
        inorder(root1, lst1)
        inorder(root2, lst2)
        i, j = 0, 0
        res = []
        while i < len(lst1) and j < len(lst2):
            if lst1[i] <= lst2[j]:
                res.append(lst1[i])
                i += 1
            else:
                res.append(lst2[j])
                j += 1
        if i < len(lst1):
            res += lst1[i:]
        elif j < len(lst2):
            res += lst2[j:]
        return res
    # brute force O[N+M log(n+m)]
    # def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
    #     tree_list = []
    #     def inorder(node):
    #         if not node:
    #             return
    #         inorder(node.left)
    #         tree_list.append(node.val)
    #         inorder(node.right)
    #     inorder(root1)
    #     inorder(root2)
    #     tree_list.sort()
    #     return tree_list
            
        