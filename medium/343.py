#!/usr/bin/python


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        res = 1
        while n:
            if n - 3 > 1:
                res *= 3
                n -= 3
            else:
                res *= n
                n = 0
        return res
        

s = Solution()
assert s.integerBreak(5) == 6
assert s.integerBreak(6) == 9
assert s.integerBreak(7) == 12
assert s.integerBreak(8) == 18
assert s.integerBreak(9) == 27
assert s.integerBreak(10) == 36
