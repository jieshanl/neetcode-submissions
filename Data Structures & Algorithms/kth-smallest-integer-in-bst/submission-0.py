# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Iterative DFS approach 
        # we know that in binary search tree (BST), left -> node -> right gives nodes in sorted order
        # use a stack to traverse nodes from left to right

        stack = [] # initialize an empty stack
        curr = root # set current node to root

        while stack or curr: # while stack is non-empty or curr is not null
            while curr: 
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right


