class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        start, end = 0, length - 1
        maximum_area = 0

        while start < end:
            maximum_area = max(maximum_area, min(height[start], height[end]) * (end - start))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
            
        return maximum_area
