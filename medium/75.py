"""
75. Sort Colors

https://leetcode.com/problems/sort-colors/
"""
from typing import List
from collections import defaultdict


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = defaultdict(int)
        for nr in nums:
            c[nr] += 1
        k = 0
        for nr in [0, 1, 2]:
            for i in range(c[nr]):
                nums[k] = nr
                k += 1


def main():
    sol = Solution()
    a = [2, 0, 2, 1, 1, 0]
    a = [2]
    print(sol.sortColors(a))
    print(a)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
