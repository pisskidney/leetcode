#!/usr/bin/python


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        firstCol = False
        for i in xrange(len(matrix)):
            if matrix[i][0] == 0:
                firstCol = True
                break
        for i in xrange(len(matrix)):
            for j in xrange(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in xrange(len(matrix)-1, -1, -1):
            for j in xrange(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if firstCol:
            for i in xrange(len(matrix)):
                matrix[i][0] = 0


s = Solution()
a = [[1, 2, 3], [0, 2, 5], [6, 9, 0]]
print a
s.setZeroes(a)
print a
