class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = res = 0
        for i in range(len(gas) - 1):
            #print("total before: " + str(total))
            total += gas[i] - cost[i]
            #print("total after: " + str(total))
            if total <= 0:
                total = 0
                res = i + 1
            #print("res after: " + str(res))
        return res