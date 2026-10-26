class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        print(f"{res=}")
        for i in range(n + 1):
            print(f"{i=}")
            cur = 0
            print(f"{cur=}")
            j = i
            while j:
                print(f"{j=}")
                j &= j - 1
                print(f"{j=}")
                cur += 1
                print(f"{cur=}")
            res[i] = cur
            print(f"{res=}")
        return res