class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted = Counter(nums).most_common()
        i = []
        for c in range(k):
            i.append(counted[c][0])
        return i