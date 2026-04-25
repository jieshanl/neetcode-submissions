# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: # base case: if root is null
            return None
        
        # swap the children
        tmp = root.left
        root.left = root.right # swap the left and right nodes
        root.right = tmp

        # recursively invert the sub-trees
        self.invertTree(root.left) # making a recursive call to the function
        self.invertTree(root.right)
        return root