# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS level-by-level approach
        # Use a queue for traversal
        # first level: [3]; second level: [20, 9];

        res = []
        q = deque([root] if root else [])

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # odd index level need to be reversed
            level = reversed(level) if len(res) % 2 else level
            res.append(level)
        return res

        # Time Complexity: O(n)
        # Space Complexity: O(n)
        
