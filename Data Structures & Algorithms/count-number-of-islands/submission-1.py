class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # count and return the number of islands
        # Use the BFS approach with O(m * n) time & space complexity

        # Brute force solution: exponential time
        #           0
        #       /       \
        #      1          1             O(4 * n)

        ROWS, COLS = len(grid), len(grid[0]) 
        visited = set() # keep track of the visited nodes
        num_islands = 0

        def bfs(r, c):
            q = deque([(r, c)])
            visited.add((r, c))

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            while q: # while q is not empty
                row, col = q.popleft() # pop the first node in queue to find its neighbors
                for dr, dc in directions:
                    neiR, neiC = row + dr, col + dc
                    if (0 <= neiR < ROWS and 0 <= neiC < COLS and
                        (neiR, neiC) not in visited and
                         grid[neiR][neiC] == "1"):
                         visited.add((neiR, neiC))
                         q.append((neiR, neiC))

                        
        # find all "1"s in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    num_islands += 1
        return num_islands