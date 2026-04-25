class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # dp approach

        # edge case: if the sum of nums is odd, immediately return False
        if sum(nums) % 2:
            return False

        # use a dp set to store the possible sums and find target
        dp = set() 
        dp.add(0) 
        target = sum(nums) // 2

        # start iterating from the last index of nums
        for i in range(len(nums) - 1, -1, -1):
            # use a nextDP set 
            nextDP = set()
            for tar in dp:
                #if (tar + nums[i]) == target:
                    #return True
                nextDP.add(tar + nums[i])
                nextDP.add(tar)
            dp = nextDP
        return True if target in dp else False



        
        