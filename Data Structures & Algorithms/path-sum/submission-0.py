# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # DFS approach, inorder binary tree traversal
        # O(n), O(n)
        def dfs(node, curSum):
            if not node: # empty tree
                return False
            curSum += node.val
            if not node.left and not node.right: # it does Not have any children
                return curSum == targetSum

            return (dfs(node.left, curSum) or dfs(node.right, curSum))

        return dfs(root, 0)


        


