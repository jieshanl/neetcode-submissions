class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # given heights, 2D array r * c
        
        ROWS, COLS = len(heights), len(heights[0])
        minHeap = [[0, 0, 0]]    # [diff, r, c]
        visit = set() # declare a hashset to track visited cells
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        # add grid cells to this minHeap
        # we will prioritize the minimum abs difference
        while minHeap:
            diff, r, c = heapq.heappop(minHeap)
        
            if (r, c) in visit:
                continue
            
            visit.add((r, c))
            if (r, c) == (ROWS - 1, COLS - 1): # if we reached the bottom right
                return diff

            # BFS to traverse neighboring cells
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 or
                    neiR == ROWS or neiC == COLS or
                    (neiR, neiC) in visit):
                    continue # continue to the next iteration of the loop
                newDiff = max(diff, abs(heights[r][c] - heights[neiR][neiC]))
                heapq.heappush(minHeap, [newDiff, neiR, neiC])






