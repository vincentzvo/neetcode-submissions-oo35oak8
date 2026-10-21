class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0             # init res to 0
        while n:            # loop while n is > 0:
            res += n % 2        # increm res by n % 2 (1 if n is odd/bin rep ends in 1)
            n >>= 1             # update n to n bit shifter right by 1
        return res          # return res