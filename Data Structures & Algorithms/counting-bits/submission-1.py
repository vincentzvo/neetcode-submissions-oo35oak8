class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(n + 1):
            cur = 0
            j = i
            while j:
                j &= j - 1
                cur += 1
            res[i] = cur
        return res