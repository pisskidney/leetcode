"""
90. Subsets II

https://leetcode.com/problems/subsets-ii/
"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        done = set([])
        nums = sorted(nums)

        def go(index, current):
            if index == len(nums):
                done.add(tuple(current))
                return
            current.append(nums[index])
            go(index+1, current)
            current.pop()
            go(index+1, current)

        go(0, [])

        powerset = [x for x in done]
        map(list, powerset)
        return powerset


def main():
    s = Solution()
    print(s.subsetsWithDup([2, 1, 2, 2, 2]))


if __name__ == '__main__':
    raise(SystemExit(main()))
