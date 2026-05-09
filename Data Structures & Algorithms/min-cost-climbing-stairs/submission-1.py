class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)                                  # append 0 to end of cost list

        for i in range(len(cost) - 3, -1, -1):          # traverse new cost list backwards, starting at 3rd to last idx
            cost[i] += min(cost[i + 1], cost[i + 2])        # to the cur idx of the cost list, add the min of the 2 idxs to the right
        
        return min(cost[0], cost[1])                    # return the min of the 1st and 2nd idxs of cost list