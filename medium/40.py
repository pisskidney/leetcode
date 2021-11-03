#!/usr/bin/python
from typing import List


"""
40. Combination Sum II

https://leetcode.com/problems/combination-sum-ii/
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)

        def go(index, current, target, last_added):
            if target < 0:
                return
            if target == 0:
                res.append(current[:])
                return
            if index >= len(candidates):
                return
            if not last_added and candidates[index] == candidates[index - 1] and index >= 1:
                return go(index+1, current, target, False)

            go(index+1, current, target, False)
            go(index+1, current + [candidates[index]], target - candidates[index], True)

        go(0, [], target, False)
        return res


class Solution2:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)

        def go(index, current, target):
            if target == 0:
                res.append(current[:])
                return
            if target < 0:
                return
            if index >= len(candidates):
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                current.append(candidates[i])
                go(i + 1, current, target - candidates[i])
                current.pop()

        go(0, [], target)

        return res


def main():
    sol = Solution()
    print(sol.combinationSum2([1] * 100, 30))
    print(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(sol.combinationSum2([1], 1))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
