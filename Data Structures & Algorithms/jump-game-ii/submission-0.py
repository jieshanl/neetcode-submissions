class Solution:
    def jump(self, nums: List[int]) -> int:
        # nums = [2, 4, 1, 1, 1, 1]
        # try using breadth first search BFS, greedy algorithm, which guarantees minimum
        # greedy, O(n)
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            # update l and r
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res



            