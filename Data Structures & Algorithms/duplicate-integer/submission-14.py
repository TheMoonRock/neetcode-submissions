class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        for item in nums:
            if item in d:
                return True
            else:
                d[item] = 1
        return False