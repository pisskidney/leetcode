#!/usr/bin/python
from typing import List


"""
34. Find First and Last Position of Element in Sorted Array

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""


class Solution:
    def find(self, nums, target, left, right, left_border=True):
        best = -1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                best = middle
                if left_border:
                    right = middle - 1
                else:
                    left = middle + 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return best

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left = self.find(nums, target, 0, len(nums) - 1, True)
        right = self.find(nums, target, 0, len(nums) - 1, False)
        return [left, right]


def main():
    sol = Solution()
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))
    print(sol.searchRange([1], 1))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
