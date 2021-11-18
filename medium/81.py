"""
81. Search in Rotated Sorted Array II

https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        def go(left, right):
            if left > right:
                return False
            middle = (left + right) // 2
            if nums[middle] == target:
                return True
            if nums[middle] < target <= nums[right]:
                return go(middle+1, right)
            elif nums[left] <= target < nums[middle]:
                return go(left, middle-1)
            return go(left, middle-1) or go(middle+1, right)

        return go(0, len(nums)-1)


def main():
    s = Solution()
    print(s.sea())


if __name__ == '__main__':
    raise(SystemExit(main()))
