class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][len(matrix[0]) - 1] < target:
                l = m + 1
            else:
                l = 0
                r = len(matrix[m]) - 1

                while l <= r:
                    m2 = (l + r) // 2
                    if matrix[m][m2] > target:
                        r = m2 - 1
                    elif matrix[m][m2] < target:
                        l = m2 + 1
                    else:
                        return True

        return False