# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # bfs approach
        
        res = 0
        q = collections.deque() # use a queue that stores pairs
        q.append((root, float("-inf"))) #[(node, maxSoFarOnPath)]

        while q:
            node, maxVal = q.popleft()
            if node.val >= maxVal:
                res += 1
            if node.left: # need to check if node.left exist
                q.append((node.left, max(maxVal, node.val)))
            if node.right: # check if node.right also exist
                q.append((node.right, max(maxVal, node.val)))
        return res


