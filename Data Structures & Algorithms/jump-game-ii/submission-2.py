class Solution:
    def jump(self, nums: List[int]) -> int:
        # try using breadth first search BFS, greedy algorithm, which guarantees minimum
        # greedy, O(n)

        # return the minimum number of jumps to reach the last position in the array

        # Decision Tree - BFS
        #               2
        #           4       1
        #   1   1   1   1   1

        res = 0
        l, r = 0, 0 # a greedy window, represent the range of indices reachable with the current number of jumps
        # [2, 4, 1, 1, 1, 1]
        #  l     r  l
        # from this range, we can find the farthest index we can reach in the next jump

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res

        # Time Complexity: O(n)
        # Space Complexity: O(1)

        

        



            