class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            stack = []
            for j in range(i, len(heights)):
                if not stack or heights[j] < stack[-1]: 
                    stack.append(heights[j])
                area = stack[-1] * (j - i + 1)
                maxArea = max(area, maxArea)
        return maxArea