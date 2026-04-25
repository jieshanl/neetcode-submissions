class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res, maxCount = 0, 0

        for num in nums:
            count[num] = count.get(num, 0) + 1
            res = num if count[num] > maxCount else res
            maxCount = max(count[num], maxCount)
        return res

        # this hashmap data structure takes O(n) memory
        # optimize the memory to O(1) with Boyer-Moore algorithm
        # 1, 2, 2, 3, 3, 1, 1
        # 1 -> 3
        # 2 -> 2
        # 3 -> 2
        