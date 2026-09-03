class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for idx, num in enumerate(nums):
            if num in d:
                return True
            d[num] = idx
        return False