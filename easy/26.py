#!/usr/bin/python


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return n
        i = 1
        for j in xrange(1, len(nums)):
            if nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i += 1
        return i


s = Solution()
x = [1, 2, 2, 2, 3, 3]
print s.removeDuplicates(x)
print x
