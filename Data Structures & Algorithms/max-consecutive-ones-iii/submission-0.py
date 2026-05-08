class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Sliding Window algorithm

        res = 0
        l = 0 # set left pointer at 0

        # iterate right pointer over len(nums)
        for r in range(len(nums)):
            # k decrement 1 if nums[r] is 0 else decrement 0
            # this for loop is essentially expanding the window size
            k -= (1 if nums[r] == 0 else 0)
            while k < 0: # this while loop is essentially shrinking the window by moving the left pointer
                k += (1 if nums[l] == 0 else 0)
                l += 1
            res = max(res, r - l + 1) 

        return res


            