class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0             # init res to 0
        while n:            # while n is > 0:
            n &= n - 1          # update n to & bit op of n and n - 1
            res += 1            # increm res
        return res          # return res