"""
35. Search Insert Position

https://leetcode.com/problems/search-insert-position/
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def go(left, right):
            if left > right:
                return left
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                return go(middle+1, right)
            return go(left, middle-1)
        return go(0, len(nums) - 1)


def main():
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 2))


if __name__ == '__main__':
    raise(SystemExit(main()))
