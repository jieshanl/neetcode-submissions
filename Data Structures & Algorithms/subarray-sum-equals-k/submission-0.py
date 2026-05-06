class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Use a hashmap 
        # The hash map must start with {0: 1} to handle subarrays 
        # that start from index 0. Without this initialization, 
        # subarrays where prefixSum == k from the beginning will not be counted.
        
        res = 0
        curSum = 0
        prefixSums = { 0 : 1}

        for n in nums:
            curSum += n
            diff = curSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = prefixSums.get(curSum, 0) + 1
        return res

        # Time Complexity: O(n)
        # Space Complexity: O(n)