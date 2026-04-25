class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # a + b + c = 0
        # Brute force would require triple loop, but inefficient with O(n**3)

        # Sort the input array in ascending order

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            # Now we're basically solving a two sum
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res