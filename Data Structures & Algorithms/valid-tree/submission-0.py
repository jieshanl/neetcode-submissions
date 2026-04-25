class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 0 - 1, 0 - 2, 0 - 3, 1 - 4
        # valid tree has to have no detected cycles and all nodes need to be connected
        # build an adjacency list for the undirected graph
        # by using BFS, we can traverse the graph level by level
        # if we ever reach a node that was already visited and is not the parent, we detect a cycle
        # after BFS, if all nodes are visited, the graph is connected
        
        # edge case: number of edges can't be greater than n - 1
        # if n = 5, number of edges can't be greater than 4
        if len(edges) > n - 1:
            return False
        adj = [[] for _ in range(n)] # adjacency list to store all neighbors of nodes 0 - 4
        
        # for loop for each u, v in edges
        for u, v in edges:
            # edge [0, 1] means 0 - 1 which means 1 is the neighbor of 0
            # edge [0, 1] also means that 0 is the neighbor of 1
            adj[u].append(v)
            adj[v].append(u)

        # Use a set to keep track of visited nodes
        visited = set()
        q = deque([(0, -1)]) # start bfs from node 0, use a queue data structure to store (current_node, parent)
        visited.add(0)

        while q: # while q is not empty
            node, parent = q.popleft() # pop (0, -1)
            for neighbor in adj[node]: # adj[0]: [1, 2, 3]
                if neighbor == parent: # check if neighbor is its parent
                    continue
                # check if neighbor is in visited, then we return False b/c we detected a cycle
                if neighbor in visited:
                    return False
                visited.add(neighbor)
                q.append((neighbor, node))
                
        return len(visited) == n

            
        



        
