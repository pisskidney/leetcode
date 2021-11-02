#!/usr/bin/python
from typing import List


"""
39. Combination Sum

https://leetcode.com/problems/combination-sum/
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def go(current_list, index, target, candidates, res):
            if index == len(candidates) or sum(current_list) == target:
                if sum(current_list) == target:
                    res.append(current_list[:])
                return

            for i in range(((target - sum(current_list)) // candidates[index]) + 1):
                current_list += [candidates[index]] * i
                go(current_list, index + 1, target, candidates, res)
                for _ in range(i):
                    current_list.pop()

        res = []
        go([], 0, target, candidates, res)
        return res


def main():
    sol = Solution()
    print(sol.combinationSum([2, 3, 5], 8))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
