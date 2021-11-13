#!/usr/bin/python
"""
63. Unique Paths II

https://leetcode.com/problems/unique-paths-ii/
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        res = [[None for _ in range(m)] for _ in range(n)]
        res[0][0] = 1
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    res[i][j] = 0
                    continue
                if i == 0 and j == 0:
                    continue
                else:
                    top = 0 if i - 1 < 0 else res[i-1][j]
                    left = 0 if j - 1 < 0 else res[i][j-1]
                    res[i][j] = top + left
        return res[n-1][m-1]


def main():
    sol = Solution()
    print(sol.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(sol.uniquePathsWithObstacles([[0, 1, 0], [0, 1, 0], [0, 0, 0]]))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
