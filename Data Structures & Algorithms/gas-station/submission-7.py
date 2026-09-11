class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):        # check if sum of gas vals < sum of cost vals:
            return -1                       # return -1 since no solution possible if true

        total = res = 0                 # init total and res to zero

        for i in range(0, len(gas)):    # traverse gas and cost lists by index:
            total += gas[i] - cost[i]       # add difference of cur gas and cost to running total
            if total < 0:                   # if total ever becomes negative after cur gas and cost:
                total = 0                       # reset total to zero
                res = i + 1                     # update res to cur idx + 1, since thats the next possible solution
        return res                      # return res that was never overwritten
        