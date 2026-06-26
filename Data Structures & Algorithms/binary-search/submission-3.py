class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Note: nums is already in ascending order
        # Binary search would give O(log n) time complexity

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return -1

        # Time complexity: O(log n)
        # Space Complexity: O(1)