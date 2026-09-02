class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        f = {}
        for num in nums:
            if num in f:
                return True
            f[num] = 1
        return False