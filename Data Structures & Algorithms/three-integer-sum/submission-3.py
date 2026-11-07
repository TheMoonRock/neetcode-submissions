class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for idx, item in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            left, right = idx + 1, len(nums) - 1
            while left < right:
                pair_sum = nums[left] + nums[right]
                if pair_sum < -item:
                    left += 1
                elif pair_sum > -item:
                    right -= 1
                elif pair_sum == -item:
                    res.append([item, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return res