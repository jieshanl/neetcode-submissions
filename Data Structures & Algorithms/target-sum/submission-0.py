class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Ex: nums = [2, 2, 2], target = 2
        # 2 - 2 + 2, 2 + 2 - 2, or -2 + 2 + 2, 3 different ways total

        n = len(nums) 
        dp = [defaultdict(int) for _ in range(n + 1)] # if n = 3 -> [[-2, 2], [-2, 2], [-2, 2], [-2, 2]]
        # defaultdict(int) will map the sum to the count
        dp[0][0] = 1 # base case, (0 elements, 0 sum) -> 1 way
                     # 1 way to sum to zero with first 0 elements
        
        for i in range(n):
            for cur_sum, count in dp[i].items(): # for cur_sum, count in that row
                dp[i + 1][cur_sum + nums[i]] += count
                dp[i + 1][cur_sum - nums[i]] += count
                
        return dp[n][target]





