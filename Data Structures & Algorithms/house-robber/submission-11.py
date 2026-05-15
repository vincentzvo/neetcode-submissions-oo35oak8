class Solution:
    def rob(self, nums: List[int]) -> int:
        l = 0
        r = 0

        for n in nums:
            temp = r
            r = max(r, n + l)
            l = temp
        return max(l, r)