# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Iteration algorithm

        if not root:
            return TreeNode(val)

        cur = root
        while cur:
            if val > cur.val:
                if not cur.right:
                    cur.right = TreeNode(val)
                    return root
                cur = cur.right
            else: # val <= cur.val
                if not cur.left:
                    cur.left = TreeNode(val)
                    return root
                cur = cur.left
        
        # Time Complexity: O(h), where h is the height of the given bst
        # Space Complexity: O(1)


