class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # given a 0-indexed array nums
        # Use Counter in Python to map the count
        # Greedy Algorithm

        count = Counter(nums) # Count[num] = c, count the frequency of each num
        res = 0

        for num, c in count.items():
            if c == 1:
                return -1
            # else: we can use the operation to delete the duplicate nums
            res += math.ceil(c / 3)
        return res

        # Time Complexity: O(n)
        # Space Complexity: O(n)