#!/usr/bin/python


'''
Calculate the path from the top left corner of a matrix to the bottom right,
such that you can only move down and right, and the sum of elements must be
as large as possible.
'''


INF = 2**32 * -1


def max_path(grid):
    dp = [[0 for _ in xrange(len(grid[0]))] for _ in xrange(len(grid))]
    dp[0][0] = grid[0][0]
    n, m = len(grid), len(grid[0])
    for i in xrange(n):
        for j in xrange(m):
            left, top = INF, INF
            if i - 1 >= 0:
                top = grid[i][j] + dp[i-1][j]
            if j - 1 >= 0:
                left = grid[i][j] + dp[i][j-1]
            if i != 0 or j != 0:
                dp[i][j] = max(left, top)
    print dp
    return dp[-1][-1]


grid = [
[3, 7, 9, 2, 7],
[9, 8, 3, 5, 5],
[1, 7, 9, 8, 5],
[3, 8, 6, 4, 10],
[6, 3, 9, 7, 8],
]
print max_path(grid)
