class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        b = []
        for num in nums:
            if num in b:
                return True
            b.append(num)
        return False