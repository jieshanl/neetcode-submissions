"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # use breadth first search BFS and a queue data structure
        curr, nxt = root, root.left if root else None

        while curr and nxt:
            curr.left.next = curr.right
            if curr.next: # check if curr.next is non-empty, then connect
                curr.right.next = curr.next.left

            curr = curr.next # update curr to curr.next, which is the start of the next level
            if not curr: # if it's empty/null
                curr = nxt
                nxt = curr.left
        return root
        

       
