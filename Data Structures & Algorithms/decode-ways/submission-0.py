class Solution:
    def numDecodings(self, s: str) -> int:
        # use bottom-up dp approach
        # Initialize cache with a hashmap
        dp = {len(s) : 1} # this basically means ...

        for i in range(len(s) - 1, -1, -1):
            # base case:
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            
            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2"
                and s[i + 1] in "0123456")):
                dp[i] += dp[i + 2]

        return dp[0]
