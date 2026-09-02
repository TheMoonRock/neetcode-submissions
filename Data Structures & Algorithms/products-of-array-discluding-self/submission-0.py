import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for index in range(len(nums)):
            m = 1
            for idx, item in enumerate(nums):
                if idx != index:
                    m = m * item
            result.append(m)
        return result