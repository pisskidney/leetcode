#!/usr/bin/python


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        mid = (low + n) / 2
        g = guess(mid)
        while g != 0:
            if g is -1:
                high = mid - 1
            if g is 1:
                low = mid + 1
            mid = (low + high) / 2
            g = guess(mid)
        return mid


def guess(x):
    if x == 1:
        return 0
    elif x > 1:
        return -1
    else:
        return 1


s = Solution()
print s.guessNumber(1)
