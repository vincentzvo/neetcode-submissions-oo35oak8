class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0             # init res to 0
        while n:            # loop while n is > 0:
            if n % 2:           # if n is odd (binary rep ends in 1):
                res += 1            # increm res
            n = n >> 1          # update n to n bit shifter right by 1
        return res          # return res