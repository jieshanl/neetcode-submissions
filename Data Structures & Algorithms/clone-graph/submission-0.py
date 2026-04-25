"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {} # Initialize a hashmap mapping new to old nodes

        def dfs(node): # a nested dfs or clone function
            if node in oldToNew: # if node already exist in hashmap
                return oldToNew[node] # return the new node that mapped to node

            copy = Node(node.val) # else we create a copy of old node
            oldToNew[node] = copy # map old node to the newly created node
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei)) # first the newly created node 
                                                # copy doesn't have any neighbors yet,
                                                # so we need to append to empty [].
            return copy # just return the connected graph is fine
        
        return dfs(node) if node else None # return dfs(node) if node is non-null else return null