class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # try the greedy approach O(n) time complexity, O(1) space 
        goal = len(nums) - 1

        # ex: [2, 3, 1, 1, 4]
        for i in range(len(nums) - 1, -1, -1): # looping backwards up until the initial index
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False