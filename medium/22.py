#!/usr/bin/python
from typing import List


"""
22. Generate Parentheses

https://leetcode.com/problems/generate-parentheses/
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def para(opened, closed, current):
            if len(current) == 2 * n:
                res.append(current)
                return
            if opened == closed:
                para(opened + 1, closed, current + '(')
            else:
                if opened < n:
                    para(opened + 1, closed, current + '(')
                if opened > closed:
                    para(opened, closed + 1, current + ')')

        para(0, 0, '')
        return res


def main():
    sol = Solution()
    print(sol.generateParenthesis(3))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
