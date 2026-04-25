class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # if k = 6, multiple include 0, 6, 12, 18, ...
        # use a HashMap data structure to map the remainder with index
        # and a prefix sum

        remainder = {0: -1} # map remainder to end index
        total = 0

        for i, num in enumerate(nums):
            total += num # Prefix Sum - Computing cumulative sums to efficiently determine subarray sums
            r = total % k # get the remainder
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True
        return False
    
    # O(n) time complexity
    # O(k) space complexity



