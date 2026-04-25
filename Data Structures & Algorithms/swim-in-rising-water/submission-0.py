class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # return the minimum amount of time it will 
        # take until it is possible to reach the bottom right square
        # Suggests a Greedy Algo - Dikjstra's Algo
        # Use the Min Heap data structure

        # We have a square n x n grid
        N = len(grid)
        visited = set()
        minH = [[grid[0][0], 0, 0]] # (time/max height, r, c)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # since we start from the top left (0, 0)
        # we need to add (0, 0) to visited
        visited.add((0, 0))
        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:
                return t
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                # check if neiR, neiC are out of bounds
                if (neiR < 0 or neiC < 0 or 
                    neiR == N or neiC == N or
                    (neiR, neiC) in visited):
                    continue
                visited.add((neiR, neiC))
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])

                
            


