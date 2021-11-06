#!/usr/bin/python
from typing import List


"""
55. Jump Game

https://leetcode.com/problems/jump-game/
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index = 0
        while index < len(nums) - 1:
            besti = 0
            best = 0
            for i in range(index + 1, min(len(nums), index + nums[index] + 1)):
                if nums[i] + i > best:
                    besti = i
                    best = nums[i] + i
            index = besti
            if best == 0:
                return False
        return True


def main():
    sol = Solution()
    # print(sol.canJump([2,3,1,1,4]))
    # print(sol.canJump([3,2,1,0,4]))
    # print(sol.canJump([0, 1]))
    # print(sol.canJump([1, 0]))
    # print(sol.canJump([0]))
    # print(sol.canJump([1]))
    # print(sol.canJump([1, 1, 1, 1, 1, 1, 0]))
    # print(sol.canJump([0, 0, 0, 0, 0]))
    # print(sol.canJump([0, 0]))
    # print(sol.canJump([3, 2, 1, 0, 0]))
    print(sol.canJump([2, 0]))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
