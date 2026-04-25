class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 2D grid
        # graph traversal algorithm; basically breadth first search

        # check if we have an empty grid
        if not grid:
            return 0

        # define the row and col
        rows, cols = len(grid), len(grid[0])
        visit = set()
        num_islands = 0

        # define helper function bfs
        def bfs(r, c):
            q = collections.deque() # [(r, c), ....]
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and 
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        # O(n x m) time complexity
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    num_islands += 1
        return num_islands

    

        
