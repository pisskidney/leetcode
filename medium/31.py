#!/usr/bin/python
from typing import List


"""
31. Next Permutation

https://leetcode.com/problems/next-permutation/
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        best = None
        for i in range(len(nums) - 1):
            smallest = 9999999
            for j in range(i + 1, len(nums)):
                if (nums[i] < nums[j] and nums[j] < smallest):
                    smallest = nums[j]
                    best = i, j

        if not best:
            nums[:] = sorted(nums)
        else:
            i, j = best
            nums[i], nums[j] = nums[j], nums[i]
            nums[:] = nums[:i+1] + sorted(nums[i+1:])


def main():
    sol = Solution()
    #   [4, 2, 2, 0, 0, 2, 3]
    #   [4, 2, 0, 2, 3, 0, 2]
    #   [4, 2, 0, 3, 0, 2, 2]
    a = [4, 2, 0, 2, 3, 2, 0]
    sol.nextPermutation(a)
    print(a)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
