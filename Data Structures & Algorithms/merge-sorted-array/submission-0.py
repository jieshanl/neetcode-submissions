class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Three Pointers algorithm
        
        # Last index nums1
        last_idx = m + n - 1

        while m > 0 and n > 0:
            if nums1[m - 1] < nums2[n - 1]:
                nums1[last_idx] = nums2[n - 1]
                n -= 1
            else: # nums1[m - 1] >= nums2[n - 1]
                nums1[last_idx] = nums1[m - 1]
                m -= 1
            last_idx -= 1 # last index in temp array should decrement regardless of the conditions above
        
        # edge case in nums2
        while n > 0:
            nums1[last_idx] = nums2[n - 1]
            n -= 1
            last_idx -= 1

        # Time Complexity: O(m + n)
        # Space Complexity: O(1)
        