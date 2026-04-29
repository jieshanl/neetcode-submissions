class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # output: return the minimum integer k such that 
        # you can eat all the bananas within h hours
        # algorithm: binary search, searching for k in all the possible k values
        # the max num in the piles array would be the max k and it's guaranteed we can finish bananas within h hours
        # Ex: [1, 4, 3, 2], k = 4, we can finish all piles in 4 hours <= 9 hours
        # All possible k values: [1, 2, 3, 4]
        # k = (0 + 3) // 2 = 1, if rate k = 2, we can finish in 1+2+2+1=6<9 hours
        # use a while loop with two pointers
        # left, right with l = 1, r = max(piles), b/c we can't have a rate k = 0

        l, r = 1, max(piles)
        res = r # set result to max(piles) which guarantees we can finish each pile in 1 hour

        while l <= r:
            k = (l + r) // 2

            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(float(pile) / k) # round up hours it takes
            if total_hours <= h: # check if total_hours satisfies the requirement
                res = k
                # since we are doing a binary search, we can move r to k - 1 to search for the min
                r = k - 1
            else: # else we have total_hours > h, we need to increase the rate, which means shift left pointer l to k + 1
                l = k + 1
        return res



                 



