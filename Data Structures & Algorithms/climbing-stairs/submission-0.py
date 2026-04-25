class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom up dp

        # base case: n <= 2, dp[1] = 1, dp[2] = 2
        if n <= 2:
            return n

        dp = [0] * (n + 1) # dp cache, all inistialized at 0
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]