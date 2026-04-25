# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Take care of base cases first
        if not subRoot:  # if subRoot is empty/null
            return True
        if not root: 
            return False
        if self.sameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
            
    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True

        if root and subRoot and root.val == subRoot.val: # if they are both non-empty and values are the same
            return (self.sameTree(root.left, subRoot.left) and
                    self.sameTree(root.right, subRoot.right))
            
        return False # one if empty one is not