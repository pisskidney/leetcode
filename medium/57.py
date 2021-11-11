#!/usr/bin/python
from typing import List


"""
57. Insert Interval

https://leetcode.com/problems/insert-interval/
"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval[0], newInterval[1]
        left = [i for i in intervals if i[1] < start]
        right = [i for i in intervals if i[0] > end]
        if left + right != intervals:
            middle = [[
                min(start, intervals[len(left)][0]),
                max(end, intervals[len(intervals) - len(right) - 1][1])
            ]]
            return left + middle + right
        return left + [newInterval] + right


def main():
    sol = Solution()
    print(sol.insert([[3, 5]], [1, 3]))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
