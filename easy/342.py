#!/usr/bin/python


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1: return True
        if num < 4: return False
        while int(num / 4) == num / 4.0:
            num /= 4
        return num == 1
        

s = Solution()
print s.isPowerOfFour(4)
print s.isPowerOfFour(23)
print s.isPowerOfFour(16)
