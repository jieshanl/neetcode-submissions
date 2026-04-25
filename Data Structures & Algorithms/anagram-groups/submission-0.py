class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagrams

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(word)
        return list(res.values())
                