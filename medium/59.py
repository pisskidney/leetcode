#!/usr/bin/python
from typing import List


"""
59. Spiral Matrix II

https://leetcode.com/problems/spiral-matrix-ii/
"""


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1
        res = [[None for _ in range(n)] for _ in range(n)]
        p = 1
        while left <= right and top <= bottom:
            for k in range(left, right + 1):
                res[top][k] = p
                p += 1
            top += 1
            for k in range(top, bottom + 1):
                res[k][right] = p
                p += 1
            right -= 1
            for k in reversed(range(left, right + 1)):
                res[bottom][k] = p
                p += 1
            bottom -= 1
            for k in reversed(range(top, bottom + 1)):
                res[k][left] = p
                p += 1
            left += 1
        return res


def main():
    sol = Solution()
    print(sol.generateMatrix(1))
    print(sol.generateMatrix(2))
    print(sol.generateMatrix(3))
    print(sol.generateMatrix(4))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
