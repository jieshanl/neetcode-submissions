# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS
        # O(p + q)

        # Take care of all the base cases
        if not p and not q: # if both are empty trees
            return True
        if not p or not q or p.val != q.val: # one of them is null and the other one is not null
            return False
        
        # recursive case
        return (self.isSameTree(p.left, q.left) and # traverse the left subtrees
                self.isSameTree(p.right, q.right)) # traverse the right subtrees

