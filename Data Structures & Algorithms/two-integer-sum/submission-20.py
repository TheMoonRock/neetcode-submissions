class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        for item in nums:
            if target - item in nums and target - item != item:
                index1 = nums.index(item)
                index2 = nums.index(target - item)
                return [index1, index2]
        """
        """
        if index1 == index2:
            for i in range(index2 + 1, len(nums)):
                if nums[i] == target - item:
                    return [index1, i]
        """
        dict = {}
        for idx, item in enumerate(nums):
            difference = target - item
            if difference in dict:
                return [dict[difference], idx]
            dict[item] = idx