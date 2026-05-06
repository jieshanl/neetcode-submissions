class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # use a hashmap to keep track of the frequency
        N = len(grid)
        count = defaultdict(int)

        for r in range(N):
            for c in range(N):
                count[grid[r][c]] += 1
        
        double, missing = 0, 0
        for num in range(1, N*N + 1):
            if count[num] == 0:
                missing = num
            if count[num] == 2:
                double = num
        return [double, missing]

        

