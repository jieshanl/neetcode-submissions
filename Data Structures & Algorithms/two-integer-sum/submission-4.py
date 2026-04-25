class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # What do you need to use when finding the target?
        # the index of the array and the corresponding number in the array
        # Use enumerate

        res = []
        for i, num in enumerate(nums):
            complement = target - num
            for j in range(i + 1, len(nums)):
                if nums[j] == complement:
                    res.extend((i, j))
        return res