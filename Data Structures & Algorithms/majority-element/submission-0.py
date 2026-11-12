class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_number = len(nums) / 2
        d = {}
        for item in nums:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        for item in d:
            if d[item] > majority_number:
                return item