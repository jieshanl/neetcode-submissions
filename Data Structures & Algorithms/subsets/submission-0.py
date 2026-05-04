class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # output: subsets without duplicates
        
        res = []
        subset = []

        def dfs(i): # starting from i
            # base case, i reached the last index
            if i >= len(nums):
                res.append(subset.copy())
                return
            # recursice case
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        
        dfs(0) # call the dfs helper function and start from index 0
        return res

        # Time Complexity: O(n * 2^n)
        # Space: O(n)