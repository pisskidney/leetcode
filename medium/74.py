#!/usr/bin/python


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        i, j = 0, len(matrix) * len(matrix[0]) - 1
        while i <= j:
            mid = (i + j) / 2
            row = mid / len(matrix[0])
            col = mid % len(matrix[0])
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                i = mid + 1
            else:
                j = mid - 1
        return False
        

s = Solution()
print s.searchMatrix(
    [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
    ],
    50
)


