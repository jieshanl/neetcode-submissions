# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # try using the depth first search DFS approach
        # O(n) time and space complexity

        # build a helper function to check each subtree
        def valid(node, left, right): # node, left and right boundaries
            if not node: # base case: if node is null or a empty binary search tree
                return True
            if not (left < node.val < right): # base case
                return False
            # else: recursive call on def valid
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        return valid(root, float("-inf"), float("inf")) # call the function from the root
