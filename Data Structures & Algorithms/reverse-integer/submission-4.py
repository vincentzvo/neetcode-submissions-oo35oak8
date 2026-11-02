class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2 ** 31 - 1   # init max and min integers
        MIN = -2 ** 31

        res = 0                                         # init res to 0
        while x:                                        # loop until x = 0:
            dig = int(math.fmod(x, 10))                     # set dig to x mod 10 cast to int to get rightmost dig
            x = int(x / 10)                                 # update x to remove rightmost dig

            if (res > MAX // 10 or                          # if cur res > max w/out last dig or
                (res == MAX // 10 and dig > MAX % 10)           # cur res = max w/out last dig and cur dig > max last dig
            ):                                              # ):
                return 0                                        # return 0
            if (res < MIN // 10 or                          # if cur res < min w/out last dig or
                (res == MIN // 10 and dig < MIN % 10)           # cur res = min w/out last dig and cur dig < min last dig
            ):                                              # ):
                return 0                                        # return 0

            res = (res * 10) + dig                          # set res to itself * 10 + dig to add dig onto end

        return res                                      # return res