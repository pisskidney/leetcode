#!/usr/bin/python
from typing import List


"""
47. Permutations II

https://leetcode.com/problems/permutations-ii/
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set([])

        def go(left, right):
            if left == right and tuple(nums) not in visited:
                res.append(nums[:])
                visited.add(tuple(nums[:]))
            for i in range(left, right + 1):
                if left == i or nums[left] != nums[i]:
                    nums[left], nums[i] = nums[i], nums[left]
                    go(left + 1, right)
                    nums[left], nums[i] = nums[i], nums[left]

        go(0, len(nums) - 1)
        return res


def main():
    sol = Solution()
    print(sol.permuteUnique([2, 2, 1, 1]))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
