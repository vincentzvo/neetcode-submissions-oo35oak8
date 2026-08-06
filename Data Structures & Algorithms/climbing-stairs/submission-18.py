class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1                 # init ways from penultimate step
        two = 1                 # init base case/default value
        for i in range(n - 1):  # loop for each step except for last 2
            temp = one          # store one in temp var
            one += two          # set one to sum op one and two
            two = temp          # set two to old one/temp
        return one              # return one