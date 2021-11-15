#!/usr/bin/python
from typing import List


"""
73. Set Matrix Zeroes

https://leetcode.com/problems/set-matrix-zeroes/
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = set([]), set([])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0


def main():
    sol = Solution()
    a = [1, 1, 1], [1, 0, 1], [1, 1, 1]
    print(sol.setZeroes(a))
    print(a)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
