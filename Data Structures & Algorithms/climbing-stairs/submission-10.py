class Solution:
    def climbStairs(self, n: int) -> int:
        l = 1
        r = 1

        for i in range(n):
            temp = r
            r += l
            l = temp
        
        return l