class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # if n = 3, we have an array consisting 1, 2, 3
        # combos include: [[1, 2], [1, 3], [2, 3]]
        
        # stimulate backtracking iteratively using an array of size k
        # to track our current combination

        res = [] # global

        # Write a backtrack helper function to pass in start and comb
        def backtrack(start, comb):
            # base case
            if len(comb) == k: # we've found a comb
                res.append(comb.copy())
                return
            # recursive case
            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()

        backtrack(1, [])
        return res
       
            


            

