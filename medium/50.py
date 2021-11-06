#!/usr/bin/python


"""
50. Pow(x, n)

https://leetcode.com/problems/powx-n/
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0

        def go(n):
            if n == 1:
                return x
            elif n == 0:
                return 1
            if n % 2 == 0:
                m = go(n // 2)
                return m * m
            m = go((n - 1) // 2)
            return x * m * m

        if n > 0:
            return go(n)
        n = abs(n)
        return 1 / go(n)


def main():
    sol = Solution()
    print(sol.myPow(2, 10))
    print(sol.myPow(2.1, 3))
    print(sol.myPow(2, -2))
    print(sol.myPow(-3, -3))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
