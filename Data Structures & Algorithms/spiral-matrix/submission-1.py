class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Iteration O(m * n), O(1)
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # get every i in the top row
            for i in range(left, right): # setting right out of bounds
                res.append(matrix[top][i]) # completed top row
            top += 1

            # get every i in the right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break
            
            # get every i in the bottom row, right to left backwards
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            
            # get every i in left col, bottom to top
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res

