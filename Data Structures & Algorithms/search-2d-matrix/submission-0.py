class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # get the dimensions of the matrix
        ROWS, COLS = len(matrix), len(matrix[0])

        # do the first binary search
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break # target is in current row
        
        if not (top <= bot):
            return False # target is not exist in matrix
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
        

        
        