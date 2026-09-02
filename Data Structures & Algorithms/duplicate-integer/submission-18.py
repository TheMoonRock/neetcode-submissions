class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for idx, num in enumerate(nums):
            if num in d:
                return True
            if num not in d:
                d[num] = idx
        return False