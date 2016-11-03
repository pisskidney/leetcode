#!/usr/bin/python


class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        i = 1
        while i * i <= n:
            i += 1
        return i - 1
       
