class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for idx, i in enumerate(nums):
            diff = target - i
            if diff in dict:
                return [dict[diff], idx]
            dict[i] = idx