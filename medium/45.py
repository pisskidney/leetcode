#!/usr/bin/python
from typing import List


"""
45. Jump Game II

https://leetcode.com/problems/jump-game-ii/
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        k = 0
        index = 0
        while index < len(nums) - 1:
            if index + nums[index] >= len(nums) - 1:
                return k + 1
            besti = None
            bestrange = 0
            for i in range(index + 1, min(index + 1 + nums[index], len(nums))):
                if i + nums[i] > bestrange:
                    besti = i
                    bestrange = i + nums[i]
            k += 1
            index = besti
        return k


def main():
    sol = Solution()
    print(sol.jump([2, 3, 1, 1, 4]))
    print(sol.jump([2, 3, 1, 1, 4, 3, 3, 2, 3, 4, 34, 2, 2, 3]))
    print(sol.jump([2, 3, 1, 1, 4, 1, 2, 3, 4, 3, 3, 2, 3, 4, 3, 2, 2, 34, 4, 5, 2, 2]))
    print(sol.jump([1, 1]))
    print(sol.jump([1, 0]))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
