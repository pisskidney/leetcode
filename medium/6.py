#!/usr/bin/python


"""
6. ZigZag Conversion

https://leetcode.com/problems/zigzag-conversion/
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows == 1:
            return s
        numRows = min(numRows, len(s))
        res = []
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                res.append(s[i::2 * numRows - 2])
            else:
                temp = [s[i]]
                for j in range(i + 2 * numRows - 2 * (i + 1), len(s), numRows * 2 - 2):
                    temp.append(s[j])
                    if j != i and j + i * 2 < len(s):
                        temp.append(s[j + i * 2])
                res.append(''.join(temp))
        return ''.join(res)


def main():
    sol = Solution()
    print(sol.convert('PAYPALISHIRING', 3))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
