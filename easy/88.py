"""
88. Merge Sorted Array

https://leetcode.com/problems/merge-sorted-array/
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            for j in reversed(range(m+n-1)):
                nums1[j], nums1[j-1] = nums1[j-1], nums1[j]
            nums1[0] = nums2[i]
            print(nums1)
            j = 0
            while j < m + i and nums1[j] > nums1[j+1]:
                nums1[j], nums1[j+1] = nums1[j+1], nums1[j]
                j += 1


def main():
    s = Solution()
    a = [1, 3, 5, 0, 0, 0]
    print(s.merge(a, 3, [2, 4, 6], 3))
    print(a)


if __name__ == '__main__':
    raise(SystemExit(main()))
