#!/usr/bin/python
from typing import List, Optional


"""
16. 3Sum Closest

https://leetcode.com/problems/3sum-closest/
"""


def bsearch(nums, left, right, res, i, j, target):
    while left <= right:
        middle = (left + right) // 2
        candidate = nums[i] + nums[j] + nums[middle]
        if res is None or abs(candidate - target) < abs(res - target):
            res = candidate
        if candidate == target:
            return res
        elif candidate > target:
            right = middle - 1
        else:
            left = middle + 1
    return res


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> Optional[int]:
        res = None
        nums = sorted(nums)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                res = bsearch(nums, j + 1, len(nums) - 1, res, i, j, target)
        return res


def main():
    sol = Solution()
    print(sol.threeSumClosest([-111, -111, 3, 6, 7, 16, 17, 18, 19], 13))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
