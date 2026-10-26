class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0                         # init res var to 0
        for i in range(32):             # loop 32 times:
            bit = (n >> i) & 1              # set/update bit var to n shifted right i times anded with 1
            res |= (bit << 31 - i)          # update res to iteself ored with bit shifted left 31 - i times
        return res                      # return res