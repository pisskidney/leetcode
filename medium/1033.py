"""
1033. Broken Calculator

https://leetcode.com/problems/broken-calculator/
"""


class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:

        def go(value: int) -> int:
            if value < startValue:
                return startValue - value
            if value == startValue:
                return 0
            if value % 2:
                return go(value + 1) + 1
            return go(value // 2) + 1

        return go(target)


def main():
    s = Solution()
    print(s.brokenCalc(1, 1000000000))


if __name__ == '__main__':
    raise(SystemExit(main()))
