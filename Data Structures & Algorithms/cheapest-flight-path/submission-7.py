class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n                 # init prices list with inf for each node
        prices[src] = 0                             # set src node price to 0

        for i in range(k + 1):                      # Loop once for each stop plus 1:
            tmpPrices = prices.copy()                   # set/update temp prices to prices copy

            for s, d, c in flights:                     # traverse each edge:
                if prices[s] == float("inf"):               # if edges src noce cant be reached:
                    continue                                    # skip to next edge
                if prices[s] + c < tmpPrices[d]:            # if price of src + cur cost < dst price:
                    tmpPrices[d] = prices[s] + c                # update dst price
            prices = tmpPrices                          # update prices list to temp prices

        return prices[dst] if prices[dst] != float("inf") else -1   # return dst price or -1