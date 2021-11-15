"""
77. Combinations

https://leetcode.com/problems/combinations/
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def go(left, k, current):
            if k == 0:
                res.append(current[:])
                return
            for i in range(left, n + 1):
                current.append(i)
                go(i+1, k-1, current)
                current.pop()
        go(1, k, [])
        return res


def main():
    sol = Solution()
    print(sol.combine(4, 2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
