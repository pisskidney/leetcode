#!/usr/bin/python


class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        b = ''
        while n > 0:
            b = str(n % 2) + b
            n /= 2
        
        if len(b) < 32:
            b = '0' * (32 - len(b)) + b

        res = 0
        for i, c in enumerate(b):
            res += 2**i * int(c)

        return res


s = Solution()

print s.reverseBits(10)
print s.reverseBits(43261596)
