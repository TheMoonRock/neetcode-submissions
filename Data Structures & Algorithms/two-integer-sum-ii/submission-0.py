class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        res_dict = {}
        for idx, item in enumerate(numbers):
            diff = target - item
            if diff in res_dict:
                return [res_dict[diff]+1, idx+1]
            res_dict[item] = idx