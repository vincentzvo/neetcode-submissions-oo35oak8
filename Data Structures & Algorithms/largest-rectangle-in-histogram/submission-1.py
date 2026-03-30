class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(height * (i - index), maxArea)
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            maxArea = max(h * (len(heights) - i), maxArea)

        return maxArea