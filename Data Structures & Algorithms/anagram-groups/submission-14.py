class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for item in strs:
            counts = [0] * 26
            for c in item:
                counts[ord(c) - ord("a")] += 1
            res[tuple(counts)].append(item)
        return list(res.values())