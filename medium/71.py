#!/usr/bin/python
"""
71. Simplify Path

https://leetcode.com/problems/simplify-path/
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        pathlist = path.split('/')
        stack = []
        for elem in pathlist:
            if not elem or elem == '.':
                continue
            elif elem == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(elem)
        return '/' + '/'.join(stack)


def main():
    sol = Solution()
    print(sol.simplifyPath('/a/./b/../../c/'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
