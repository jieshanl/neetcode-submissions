class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            complement = target - nums[i]
            for j, num in enumerate(nums):
                if num == complement and j != i:
                    return [i, j]