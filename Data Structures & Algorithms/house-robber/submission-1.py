class Solution:
    def rob(self, nums: List[int]) -> int:
        l = 0
        r = 0

        for n in nums:
            temp = max(n + l, r)
            l = r
            r = temp
        return r