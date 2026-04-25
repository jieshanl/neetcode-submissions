class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # brute force solution:
        # start with a left pointer at index 0 and iterate right pointer in the array
        # use prefix sum to precompute cumulative sums 

        """res = 0 # count the number of sub arrays
        l = 0

        for r in range(k - 1, len(arr)): # approximately size n
            preSum = 0
            for i in range(l, r + 1): # size k
                preSum += arr[i]

            if preSum / k >= threshold:
                res += 1
            
            l += 1 # we need to increment the left pointer after finishing iterating through every single value in the current window

        
        return res"""
    
    # for this brute force solution, we have O(n * k) time complexity, and O(1) space complexity

        # Optimization: initialize the window outside of the loop, sliding window
        
        res = 0 # track the number of sub arrays that satisfy the conditions
        curSum = sum(arr[:k-1]) # prefix sum already calculated the sum of window k - 1

        for l in range(len(arr) - k + 1):
            curSum += arr[l + k - 1]
            if (curSum / k) >= threshold:
                res += 1
            curSum -= arr[l]
        
        return res

    # this optimized solution would only take O(n) or linear time complexity












