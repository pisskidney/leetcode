#!/usr/bin/python


"""
43. Multiply Strings

https://leetcode.com/problems/multiply-strings/
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        res = [0] * (len(num1) + len(num2))
        for i in reversed(range(len(num2))):
            cf = 0
            for j in reversed(range(len(num1))):
                mult = int(num2[i]) * int(num1[j]) + res[i + j + 1] + cf
                res[i + j + 1] = mult % 10
                cf = mult // 10
            if cf:
                res[i] = cf

        if res[0] == 0:
            res = res[1:]

        return ''.join([str(x) for x in res])


def main():
    sol = Solution()
    print(sol.multiply('99', '9'))
    print(sol.multiply('99', '9999'))
    print(sol.multiply('10', '100'))
    print(sol.multiply('1', '99900'))
    print(sol.multiply('99000', '1'))
    print(sol.multiply('1', '1'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
