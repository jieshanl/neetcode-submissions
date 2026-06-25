class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check this edge case: when length of s and length of t are not equal
        if len(s) != len(t):
            return False # immediately return False
        
        # Create two hash maps to store character frequencies for each string.
        countS = {}
        countT = {}

        # Iterate through s and increase the character count
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        # finally, compare both hashmaps
        return countS == countT

        # Time Complexity: O(n + m)
        # Space Complexity: O(1)




        
