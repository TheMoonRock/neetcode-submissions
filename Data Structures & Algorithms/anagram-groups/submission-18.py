class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d= defaultdict(list)

        for word in strs:
            k = [0] * 26
            for c in word:
                k[ord(c) - ord("a")] += 1
            d[tuple(k)].append(word)
        return list(d.values())