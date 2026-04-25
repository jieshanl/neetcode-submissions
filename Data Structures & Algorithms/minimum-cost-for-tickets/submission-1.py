class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Try using bottom-up DP, which is iterative
        # O(n) time and space complexity

        n = len(days) # [1, 2, 8] len = 3
        dp = [0] * (n + 1) # initializa a dp or cache [0, 0, 0, 0]

        for i in range(n - 1, -1, -1): # start from the last day index
            dp[i] = float("inf") # set dp[i] at infinitely large first ["inf"]
            j = i 
            for d, c in zip([1, 7, 30], costs):
                while j < n and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dp[j])

        return dp[0]




        