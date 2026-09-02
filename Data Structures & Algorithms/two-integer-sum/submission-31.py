class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, item in enumerate(nums):
            diff = target - item
            if diff in d:
                return [d[diff], idx]
            else:
                d[item] = idx