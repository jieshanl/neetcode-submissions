class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set() # to make sure we don't revisit the same position twice within our path

        def dfs(r, c, i):
            # r, c is the current row, column that we are visiting
            # i represents the index of the word we are searching

            if i == len(word):
                return True
            
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or
                word[i] != board[r][c] or (r, c) in path):
                return False
            
            path.add((r, c)) # Mark (r, c) as visited.
            # Recurse to 4 neighbors with i + 1; recursice dfs
            res = (dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or  
                    dfs(r, c - 1, i + 1)) 
            path.remove((r, c)) # Unmark (r, c) (backtrack).
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False




            


        