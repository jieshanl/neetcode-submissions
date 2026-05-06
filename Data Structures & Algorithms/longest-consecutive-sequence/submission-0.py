class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # hashset algorithm

        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if n is the start
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

        # Time Complexity: O(n)
        # Space Complexity: O(n)