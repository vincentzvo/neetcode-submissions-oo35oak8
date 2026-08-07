class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = cost[0], cost[1]
        for i in range(2, len(cost)):
            cost[i] = min(cost[i - 1] + cost[i], cost[i - 2] + cost[i])
        return min(cost[len(cost) - 2], cost[len(cost) - 1])