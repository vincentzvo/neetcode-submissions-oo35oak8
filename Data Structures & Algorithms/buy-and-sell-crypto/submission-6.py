class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]
        for p in prices:
            buy = min(buy, p)
            res = max(res, p - buy)
        return res