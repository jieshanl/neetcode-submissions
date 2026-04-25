class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seen = defaultdict(int)
        for c in s:
            seen[c] += 1
        for c in t:
            seen[c] -= 1
            if seen[c] < 0:
                return False
        return True
        
