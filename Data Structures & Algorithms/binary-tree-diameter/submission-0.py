# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # create a nested function dfs
        # returns the height of a tree, not the diameter
        res = 0

        def dfs(curr):
            # base case
            if not curr:
                return 0
            # recursive case
            left = dfs(curr.left)
            right = dfs(curr.right)

            nonlocal res
            res = max(res, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return res