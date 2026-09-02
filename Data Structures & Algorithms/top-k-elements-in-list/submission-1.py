class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted = Counter(nums).most_common()
        l = []
        for c in range(k):
            l.append(counted[c][0])
        return l