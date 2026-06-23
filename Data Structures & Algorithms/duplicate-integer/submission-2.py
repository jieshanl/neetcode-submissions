class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # initialize an empty set "seen"

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False