class Solution:
    def climbStairs(self, n: int) -> int:
        l = 1
        r = 1

        for i in range(n):
            temp = l
            l += r
            r = temp
        return r