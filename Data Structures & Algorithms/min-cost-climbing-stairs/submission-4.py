class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = cost[0], cost[1]
        for i in range(2, len(cost)):
            temp = two
            two = min(two + cost[i], one + cost[i])
            one = temp
        return min(one, two)