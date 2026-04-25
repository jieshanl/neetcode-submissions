# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # use BFS traversal algorithm

        res = []
        q = collections.deque() # initialize a queue to note the current visiting node
        q.append(root) # we are currently visiting root

        while q: # while queue is not empty
            qlength = len(q) # length would be 1 right now
            level = [] # append level by level
            for i in range(qlength):
                node = q.popleft()
                if node: # if node is not null
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level: # if level is non-empty
                res.append(level)

        return res


