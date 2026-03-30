class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most = 0
        for i, h in enumerate(heights):
            l = i
            r = l + 1
            water = 0
            while r < len(heights):
                water = (r - l) * min(heights[l], heights[r])
                most = max(water, most)
                r += 1
        return most