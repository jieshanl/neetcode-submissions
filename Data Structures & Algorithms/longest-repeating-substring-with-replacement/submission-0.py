class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # use a hashmap to keep track of frequency
        res = 0 # the length of the longest substring

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res

        # O(n) time