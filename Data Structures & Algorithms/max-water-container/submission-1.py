class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            water = (r - l) * min(heights[l], heights[r])
            most = max(water, most)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return most