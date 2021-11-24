"""
89. Gray Code

https://leetcode.com/problems/gray-code/
"""
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            res += [x + 2**i for x in reversed(res)]
        return res


def main():
    s = Solution()
    print(s.grayCode(3))


if __name__ == '__main__':
    raise(SystemExit(main()))
