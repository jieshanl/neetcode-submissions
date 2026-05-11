class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Word1 = "abc" -> base case
        # Word2 = "" -> base case
        # number of operations would be the length of Word1

        # Bottom-Up DP
        # 2D cache

        cache = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        # fill up the bottom row and rightmost column of 2D dp
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i
        
        # iterate through the 2D DP table backwards
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    cache[i][j] = 1 + min(cache[i + 1][j + 1], cache[i + 1][j], cache[i][j + 1])
        
        return cache[0][0]

        # Time Complexity: O(m * n)
        # Space Complexity: O(m * n)


        
