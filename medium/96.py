"""
96. Unique Binary Search Trees

https://leetcode.com/problems/unique-binary-search-trees/
"""


class Solution:
    def numTrees(self, n: int) -> int:

        memo = {}

        def go(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            if left == right:
                return 1
            if left > right:
                return 1
            acc = 0
            for i in range(left, right+1):
                leftval = go(left, i-1)
                rightval = go(i+1, right)
                acc += leftval * rightval
            memo[(left, right)] = acc
            return acc

        return go(1, n)


def main():
    s = Solution()
    print(s.numTrees(20))


if __name__ == '__main__':
    raise(SystemExit(main()))
