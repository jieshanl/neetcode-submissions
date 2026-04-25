class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS approach
        # grid = [[1,0,1],
        #         [0,2,0],
        #         [1,0,1]]

        ROWS, COLS = len(grid), len(grid[0])
        # Initialize a queue with positions of all rotten organges
        q = collections.deque()
        fresh_org_count = 0 # start fresh at 0
        time = 0 # we start at 0 minutes and increment as we go

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_org_count += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh_org_count > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                # for each available rotten organge, traverse it's neighbors
                for dr, dc in directions:
                    neiR, neiC = r + dr, c + dc
                    if (0 <= neiR < ROWS and 0 <= neiC < COLS and
                        grid[neiR][neiC] == 1):
                        grid[neiR][neiC] = 2 # fresh bacomes rotten
                        q.append((neiR, neiC))
                        fresh_org_count -= 1
            time += 1
        return time if fresh_org_count == 0 else -1
                        
       




