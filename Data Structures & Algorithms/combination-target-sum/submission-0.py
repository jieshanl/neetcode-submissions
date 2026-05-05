class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # output: return a list of all unique combination of nums
        # where the chosen numbers sum to target

        # use the backtracking algorithm

        res = []
    
        # define a helper dfs function to run deapth first search on the decision tree
        #                   [] -> this is cur_comb
        #               /       \
        #           [2]           []
        #           / \           / \ 
        #       [2, 2] [2]      [5]  []
        #        /  \                / \
        # [2, 2, 2] [2, 2]         [6]  []
        #    /       /   \              / \
        #  8   [2, 2, 5]  [2, 2]      [9]  [] (base case: we ran out of elements)
        #                   / \
        #                 10   13

        # i indicate the pointer in nums list
        # cur_comb is the current combination array we are appending
        # total is the number we use to maintaining the toal sum
        def dfs(i, cur_comb, total):
            # base case: if total is equal to target
            if total == target:
                res.append(cur_comb.copy())
                return # we've found the combination list and break out
            # another base case: if i is out of bounds or total is greater than target
            if i >= len(nums) or total > target:
                return # break out of this function

            # recursive case: two decisions
            cur_comb.append(nums[i])
            dfs(i, cur_comb, total + nums[i])
            cur_comb.pop()
            dfs(i + 1, cur_comb, total)

        # call dfs
        dfs(0, [], 0)
        return res

        # Time complexity: O(2^t), t is the target
        # Space: O(t)



