class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for idx, item in enumerate(nums):
            diff = target - item
            if diff in dict:
                return [dict[diff], idx]
            dict[item] = idx