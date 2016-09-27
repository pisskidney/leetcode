#!/usr/bin/python


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j


s = Solution()
x = [3, 3, 3, 3, 3, 3, 3]
print x
print s.removeElement(x, 3)
print x
