#!/usr/bin/python


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [nums[0]]
        for i in xrange(1, len(nums)):
            res.append(res[i-1] * nums[i])
        right = 1
        for i in xrange(len(nums)-1, 0, -1):
            res[i] = res[i-1] * right
            right *= nums[i]
        res[0] = right

        return res


s = Solution()
print s.productExceptSelf([2, 3])
