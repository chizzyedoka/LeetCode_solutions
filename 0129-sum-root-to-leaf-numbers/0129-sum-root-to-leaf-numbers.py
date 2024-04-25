# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        sum_stack = [0]
        total = 0
        while stack:
            node = stack.pop()
            cur_sum= sum_stack.pop()
            cur_sum = cur_sum*10 + node.val
            if node.right:
                stack.append(node.right)
                sum_stack.append(cur_sum)
            if node.left:
                stack.append(node.left)
                sum_stack.append(cur_sum)
            if not node.left and not node.right:
                total += cur_sum
        return total
                
            
    # def sumNumbers(self, root: Optional[TreeNode]) -> int:
    #     def dfs(root, cur_sum):
    #         if not root:
    #             return 0
    #         cur_sum = cur_sum*10 + root.val
    #         if not root.left and not root.right:
    #             return cur_sum
    #         left_sum = dfs(root.left, cur_sum)
    #         right_sum = dfs(root.right, cur_sum)
    #         return left_sum + right_sum
    #     return dfs(root, 0)
        