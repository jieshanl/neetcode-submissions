class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Try to use bottom-up dynamic programming
        # bottom-up dp is iterative

        dp = {}

        def dfs(i):
            if i == len(days):
                return 0
            if i in dp:
                return dp[i]

            dp[i] = float("inf")
            # run a for loop to scan through the day and costs:
            for d, c in zip([1, 7, 30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + d: # while j is not out of bounds and days at index j is less than days at index i + day d
                    j += 1
                dp[i] = min(dp[i], c + dfs(j))
            return dp[i]

        return dfs(0)

            # ex: [1, 2, 8] if you buy a 7 day pass at dat 1, you cover from day 1 to day 7
