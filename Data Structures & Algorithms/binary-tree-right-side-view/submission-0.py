# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Depth first search recursive approach
        # if we are visiting the right subtree, we need to add self.right to result
        # if we are visiting the left subtree, we need to make sure self.right is null and self.left is non-null
        # if we are visiting the left subtree, the right subtree on the same level has to be null

        res = []

        # define a nested helper dfs function
        def dfs(node, depth):
            if not node: # if node is null
                return None
            if depth == len(res): # if we start at the root, depth would be 0
                res.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0) # call healper function dfs on root
        return res
                

        
       


        

        