class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # use a two pointer method

        # start with l = 1 since the 0th index num is always unique
        # we wanna compare the r pointer num with the one before it

        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l
