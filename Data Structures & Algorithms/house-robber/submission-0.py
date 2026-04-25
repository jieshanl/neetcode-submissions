class Solution:
    def rob(self, nums: List[int]) -> int:
        # top-down DP approach

        memo = [-1] * len(nums)

        # use depth first search dfs to traverse i
        def dfs(i):
            if i >= len(nums): # if index i is out of bounds
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return memo[i]
            
        return dfs(0)
            