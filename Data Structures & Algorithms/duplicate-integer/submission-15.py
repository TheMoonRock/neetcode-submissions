class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        for idx, item in enumerate(nums):
            if item in d:
                return True
            d[item] = idx
        return False