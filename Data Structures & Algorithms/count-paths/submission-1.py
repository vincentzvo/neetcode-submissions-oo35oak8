class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rowBelow = [1] * n                                  # init bottom row with all 1s

        for i in range(m - 1):                              # loop thru all rows except last:
            curRow = [1] * n                                    # init new row same as bottom
            for j in range(n - 2, -1, -1):                      # trav each cell in cur row from sec last backwards:
                curRow[j] = curRow[j + 1] + rowBelow[j]              # set cell in cur row to prev in cur row + in row below
            rowBelow = curRow                                   # set row below to cur row
        return rowBelow[0]                                  # return first val in row below list