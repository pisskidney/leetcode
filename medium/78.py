"""
78. Subsets

https://leetcode.com/problems/subsets/
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def go(left, current):
            if left >= len(nums):
                res.append(current[:])
                return
            current.append(nums[left])
            go(left + 1, current)
            current.pop()
            go(left + 1, current)

        go(0, [])
        return res


def main():
    sol = Solution()
    print(sol.subsets([1, 2, 3]))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
