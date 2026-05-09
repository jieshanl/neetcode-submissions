class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # detect a cycle
        # any edge in the connected cyclen could be removed

        N = len(edges)
        # set parent of i to itself
        par = [i for i in range(N + 1)]
        # need to maintain a rank for two nodes
        rank = [1] * (N + 1) # set the rank of each node at 1 

        def find(n): # this find function helps find the root parent of node n and path compression
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]

        def union(n1, n2): # this union function connect two nodes together
            p1, p2 = find(n1), find(n2)

            if p1 == p2: # we detected a cycle
                return False
            # we compare the rank of n1 and n2 and connect them
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        # run a for loop to iterate n1, n2 of the edges
        for n1, n2 in edges:
            # check if we could union n1 and n2
            if not union(n1, n2): # can't union them cuz they have the same parent
                return [n1, n2] 
