#!/usr/bin/python
"""
62. Unique Paths

https://leetcode.com/problems/unique-paths/
"""


import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m -= 1
        n -= 1
        return math.factorial(m + n) // (math.factorial(m) * math.factorial(n))


def main():
    sol = Solution()
    print(sol.uniquePaths(4, 3))
    print(sol.uniquePaths(1, 1))
    print(sol.uniquePaths(7, 3))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
