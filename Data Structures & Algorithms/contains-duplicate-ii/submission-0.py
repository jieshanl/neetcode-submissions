class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set() # use a hashset to keep track of the unique values in curr window
        L = 0 # Initialize left pointer at index 0

        # use a for loop to iterate Right pointer R
        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1 # increment the left pointer by 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False


    # This solution takes O(n) time complexity
