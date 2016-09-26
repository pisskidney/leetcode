#!/usr/bin/python


class Solution(object):
    def generate(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        from operator import add
        if n is 0:
            return []
        res = [[1]]
        for i in xrange(n-1):
            res.append(map(add, res[-1] + [0], [0] + res[-1]))
        return res


s = Solution()
print s.generate(1)
