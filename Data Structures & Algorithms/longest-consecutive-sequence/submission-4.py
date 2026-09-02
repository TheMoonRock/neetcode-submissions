class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        input = sorted(set(nums))

        seq_count = 0
        res = 0

        for item in input:
            if (item + 1) in input:
                seq_count += 1
            else:
                if seq_count > res:
                    res = seq_count
                    seq_count = 0
                else:
                    seq_count = 0
        return (res+1)