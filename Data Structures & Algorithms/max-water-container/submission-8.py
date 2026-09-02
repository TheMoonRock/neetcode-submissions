class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights) - 1
        i = 0
        res = 0

        while i < length:
            area = min(heights[i], heights[length]) * (length - i)
            res = max(res, area)
            if heights[i] <= heights[length]:
                i += 1
            else:
                length -= 1
        return res