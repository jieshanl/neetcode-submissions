class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # m x n 2D grid
        # 4 directions
        # modify grid in-place

        # Multi-Source BFS from the treasure chests
        # explore level-by-level
        # line up the neighbors of the treasure chests in a queue

        rows, cols = len(grid), len(grid[0])
        visited = set() # use a visit set to track the visited grid
        q = deque() # add all the treasure cells into the queue to traverse BFS

        def addCell(r, c):
            # check if grid[r][c] indices are in bounds
            if (min(r, c) < 0 or r == rows or c == cols or 
                (r, c) in visited or grid[r][c] == -1):
                return # immediately return b/c invalid
            visited.add((r, c))
            q.append([r, c])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1

    # Time Complexity: O(m * n)
    # Space Complexity: O(m * n)





        