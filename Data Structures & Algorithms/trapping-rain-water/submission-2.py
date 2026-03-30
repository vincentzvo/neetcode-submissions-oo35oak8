class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = []
        maxR = [0] * len(height)
        minLR = [0] * len(height)
        res = 0

        curMax = 0
        for h in height:
            maxL.append(curMax)
            if h > curMax:
                curMax = h

        curMax = 0
        for i in range(len(height) - 1, -1, -1):
            maxR[i] = curMax
            if height[i] > curMax:
                curMax = height[i]
        
        for i in range(len(height)):
            minLR[i] = min(maxL[i], maxR[i])
            res += max(minLR[i] - height[i], 0)
        
        return res