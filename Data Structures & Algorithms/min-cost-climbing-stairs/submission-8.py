class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # loop for each val in cost exept starting poses
        for i in range(2, len(cost)):
            # replace cost i w/ min cost to get there 
            cost[i] = min(cost[i - 1] + cost[i], cost[i - 2] + cost[i])
        # return min of last 2 cost vals since both of those can finish climbing w/out extra cost
        return min(cost[len(cost) - 2], cost[len(cost) - 1])