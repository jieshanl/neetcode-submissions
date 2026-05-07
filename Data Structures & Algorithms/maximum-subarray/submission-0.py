class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # basically the kadane's algorithm

        # Initialize maxSum to the first value in nums by default and curSum to 0
        maxSum = nums[0]
        curSum = 0

        for num in nums:
            # check if curSum is now negative, then we reset curSum to 0
            if curSum < 0:
                curSum = 0
            # else we increment curSum with mum
            curSum += num
            maxSum = max(maxSum, curSum)
        return maxSum

        # This Kadane's Algorithm would only take O(n) time and constant space
