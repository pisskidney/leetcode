#!/usr/bin/python
from typing import List


"""
15. 3Sum

https://leetcode.com/problems/3sum/
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set([])
        count = {}
        for i, num in enumerate(nums):
            count[num] = i
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                needed = -(nums[i] + nums[j])
                sol = tuple(sorted([nums[i], nums[j], needed]))
                if (
                    needed in count and
                    count[needed] > i and
                    count[needed] > j and
                    sol not in visited
                ):
                    res.append(sol)
                    visited.add(sol)
        return res


def main():
    sol = Solution()
    print(sol.threeSum('babad'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
