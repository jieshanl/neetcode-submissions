class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set for substring
        # sliding window method
        # O(n) time and O(n) space
        substring_set = set() # {z, x, y}
        l = 0
        
        res = 0
        for r in range(len(s)):
            while s[r] in substring_set:
                substring_set.remove(s[l])
                l += 1
            substring_set.add(s[r])
            res = max(res, r - l + 1)
        return res
