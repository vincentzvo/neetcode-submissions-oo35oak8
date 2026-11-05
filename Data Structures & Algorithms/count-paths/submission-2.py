class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rowBelow = [1] * n
        for i in range(m - 2, -1, -1):
            curRow = [1] * n
            for j in range(n - 2, -1, -1):
                curRow[j] = curRow[j + 1] + rowBelow[j]
            rowBelow = curRow
        return rowBelow[0]