class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = 0
        left, right = 0, len(heights) - 1
        while left < right:
            width = right - left
            volume = width * min(heights[left], heights[right])
            max_volume = max(max_volume, volume)
            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                left += 1
                right -= 1
        return max_volume