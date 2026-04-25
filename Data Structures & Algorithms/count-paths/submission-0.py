class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m x n grid, move either down or ro the right
        # 2 x 2 grid
        # [[0 1],
        #  [1 2]]
        # brute force would be using recursion which would take O(n^ (m + n)) time
        # use the bottom-up dp approach

        dp = [[0] * (n + 1) for _ in range(m + 1)] # initialize a dp cache
        dp[m - 1][n - 1] = 1 # 1 unique path to destination from destination itself

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # break it down into subproblems by using dp
                dp[i][j] += dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]