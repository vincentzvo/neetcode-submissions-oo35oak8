class Solution:
    def reverse(self, x: int) -> int:
        strRes = ""
        flag = False
        for d in str(x)[::-1]:
            if d == "-":
                flag = True
                continue
            strRes += d
        
        if flag:
            strRes = "-" + strRes

        res = int(strRes)
        if res <= (2 ** 31 - 1) and res >= (-2 ** 31):
            return res
        else:
            return 0