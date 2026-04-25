class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # image = [[1,1,1],
        #          [1,1,0],
        #          [1,0,1]]
        # BFS approach

        # edge case, already the pixel of the color
        orig = image[sr][sc]
        if orig == color:
            return image

        ROWS, COLS = len(image), len(image[0])
        q = deque([(sr, sc)])
        image[sr][sc] = color
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if 0 <= row < ROWS and 0 <= col < COLS and image[row][col] == orig:
                    image[row][col] = color
                    q.append((row, col))

        return image
                

                