#!/usr/bin/python
from typing import List


"""
56. Merge Intervals

https://leetcode.com/problems/merge-intervals/
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        start = intervals[0][0]
        maxright = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] > intervals[i-1][1]:
                res.append([start, maxright])
                start = intervals[i][0]
                maxright = intervals[i][1]
            maxright = max(maxright, intervals[i][1])
        if not res or res[-1][0] < start:
            res.append([start, maxright])
        return res


def main():
    sol = Solution()
    print(sol.merge([[1, 2]]))
    print(sol.merge([[1, 2], [3, 4]]))
    print(sol.merge([[1, 2], [2, 4]]))
    print(sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(sol.merge([[1, 10], [2, 6], [3, 5]]))
    print(sol.merge([[1, 10], [2, 6], [3, 5], [3, 20]]))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
