"""
80. Remove Duplicates from Sorted Array II

https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = 0
        for num in nums:
            if last < 2 or num > nums[last-2]:
                nums[last] = num
                last += 1
        return last


# Shitty solution (n^2)
class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 2
        if len(nums) <= 2:
            return len(nums)
        k = 0
        while left < len(nums) - k:
            while (
                left < len(nums) - k and
                (nums[left] != nums[left-1] or nums[left-1] != nums[left-2])
            ):
                left += 1
            if left >= len(nums) - k:
                break
            for i in range(left, len(nums) - 1):
                nums[i], nums[i+1] = nums[i+1], nums[i]
            k += 1

        return len(nums) - k


def main():
    s = Solution()
    print(s.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
    print(s.removeDuplicates([0, 1, 2, 3, 4]))
    print(s.removeDuplicates([0, 0, 1, 2, 3, 4, 4, 4]))


if __name__ == '__main__':
    raise(SystemExit(main()))
