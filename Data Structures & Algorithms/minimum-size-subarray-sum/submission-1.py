class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float("inf") # initialize a really large length to be compare of later
        L = 0 # initialize left pointer at 0th index
        curSum = 0

        # iterate the right pointer in nums
        for R in range(len(nums)): # this iteration takes n time
            curSum += nums[R]
            while curSum >= target: # this takes n time in total
                length = min(length, R - L + 1)
                curSum -= nums[L]
                L += 1
            
        return 0 if length == float("inf") else length

        # This sliding window solution takes O(n) time 
        # because outer for loop takes n time and inner while loop takes n time
        # so n + n = 2n ~= n
