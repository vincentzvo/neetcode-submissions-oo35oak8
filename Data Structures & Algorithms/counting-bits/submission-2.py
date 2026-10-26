class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            cur = 0
            j = i
            while j:
                j &= j - 1
                cur += 1
            res.append(cur)
        return res