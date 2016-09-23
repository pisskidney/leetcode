#!/usr/bin/python

class Solution(object):
    def getRow(self, n):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        k = 0
        res = [1]
        while k < n:
            temp = 1
            for i in xrange(1, len(res)):
                res[i], temp = temp + res[i], res[i]
            res.append(1)
            k += 1
        return res

s = Solution()
print s.getRow(1)
