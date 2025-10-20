class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = float("-inf")
        while l < r:
            depth = min(height[l], height[r])
            width = r -l 
            area = depth * width
            max_area = max(max_area, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
