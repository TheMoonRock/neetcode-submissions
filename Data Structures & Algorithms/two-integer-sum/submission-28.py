class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for idx, item in enumerate(nums):
            diff = target - item
            if diff in res:
                return [res[diff], idx]
            res[item] = idx