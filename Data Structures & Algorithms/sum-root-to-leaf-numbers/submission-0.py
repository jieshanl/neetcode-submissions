# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Use the Depth-First-Search algorithm
        def dfs(cur_node, num):
            # base case: if cur is null
            if not cur_node:
                return 0
            
            num = num * 10 + cur_node.val
            # if cur_node is a leaf node
            if not cur_node.left and not cur_node.right:
                return num
            return dfs(cur_node.left, num) + dfs(cur_node.right, num)

        return dfs(root, 0)

    # dry run
    #       1
    #     /    \
    #   2        3
    # num = 0 * 10 + 1 = 1
    # dfs(2, 1) + dfs(3, 1)
    # num = 1 * 10 + 2 = 12
    # num = 1 * 10 + 3 = 13
    # result is 12 + 13 
