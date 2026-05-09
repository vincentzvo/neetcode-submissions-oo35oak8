class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1                     # init idx 1 and 2 to 1
        two = 1

        for i in range(n - 1):      # for each step:
            temp = one                  # store one in temp var
            one = one + two             # update one to one + two
            two = temp                  # update two to old one/temp
        
        return one                  # return one
