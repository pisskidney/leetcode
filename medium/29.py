#!/usr/bin/python


"""
29. Divide Two Integers

https://leetcode.com/problems/divide-two-integers/
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        first = second = False
        if dividend < 0:
            first = True
        if divisor < 0:
            second = True
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            j = 1
            temp = divisor
            while (temp << 1) <= dividend:
                j <<= 1
                temp <<= 1
            res += j
            dividend -= temp
        if first ^ second:
            res *= -1
        return min(2147483647, max(-2147483648, res))


def main():
    sol = Solution()
    print(sol.divide(7, 3))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
