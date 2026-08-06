class Solution:
    def climbStairs(self, n: int) -> int:
        l = 1
        r = 1
        for i in range(n - 1):
            temp = l
            l += r
            r = temp
        return l