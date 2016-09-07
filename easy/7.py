#!/usr/bin/python


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        from math import log
        
        if x < 10 and x > -10:
            return x

        flipped = False
        if x < 0:
            flipped = True
            x *= -1
        
        res = 0
        log10 = int(log(x, 10))
        for i in xrange(log10 + 1):
            digit = x % 10
            res += digit * 10**(log10 - i)
            x /= 10

        if res > 2**31 - 1 or res < -1 * 2**31 + 1:
            return 0

        if flipped:
            res *= -1

        return res
        

s = Solution()

assert s.reverse(1) == 1
assert s.reverse(12) == 21
assert s.reverse(0) == 0
assert s.reverse(123456789) == 987654321

assert s.reverse(20) == 2
assert s.reverse(201) == 102
assert s.reverse(2000) == 2

assert s.reverse(-1) == -1
assert s.reverse(-12) == -21
assert s.reverse(-123456789) == -987654321
