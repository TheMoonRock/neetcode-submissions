class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights) - 1
        i = 0
        res = 0

        while i < length and length != 0:

            if heights[i] < heights[length]:
                tmp = heights[i] * (length - i)
            else:
                tmp = heights[length] * (length - i)
            print(tmp, heights[i], heights[length])
            if tmp > res:
                res = tmp

            if i + 1 == length:
                i = 0
                length -= 1
            else:
                i += 1
        return res