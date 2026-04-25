class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int: 
       # BFS approach
       # find all rotten fruits
       # need a queue for rotten fruits to run bfs for its neighbors
       # find all fresh fruits

       ROWS, COLS = len(grid), len(grid[0])
       time = 0
       fresh_fruit_cnt = 0
       q = deque() # initialize a queue to store all rotten fruits

       # run for loops on the grid to find all the rotten fruits and fresh fruits
       for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 2:
                q.append((r, c))
            if grid[r][c] == 1:
                fresh_fruit_cnt += 1

       directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
       while q and fresh_fruit_cnt > 0:
            # Process all currently rotten oranges in one "minute"
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions: 
                    neiR, neiC = r + dr, c + dc
                    if (0 <= neiR < ROWS and 0 <= neiC < COLS and
                        grid[neiR][neiC] == 1):
                        grid[neiR][neiC] = 2
                        fresh_fruit_cnt -= 1
                        q.append((neiR, neiC))
            time += 1
        
       return time if fresh_fruit_cnt == 0 else -1