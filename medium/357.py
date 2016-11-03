#!/usr/bin/python


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n is 0:
            return 1
        if n is 1:
            return 10
        n = min(n, 10)
        res = 1
        for i in xrange(n):
            res *= 10 - i
        return res + 1


s = Solution()
print s.countNumbersWithUniqueDigits(3)

