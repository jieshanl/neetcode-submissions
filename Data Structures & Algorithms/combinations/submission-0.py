class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # if n = 3, we have an array consisting 1, 2, 3
        # combos include: [[1, 2], [1, 3], [2, 3]]
        
        # stimulate backtracking iteratively using an array of size k
        # to track our current combination

        res = []
        i = 0
        combo = [0] * k # [0, 0]

        while i >= 0:
            combo[i] += 1
            if combo[i] > n:
                i -= 1
                continue
            
            if i == k - 1:
                res.append(combo.copy())
            else:
                i += 1
                combo[i] = combo[i - 1]
                
        return res
            


            

