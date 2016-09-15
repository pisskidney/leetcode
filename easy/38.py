#!/usr/bin/python


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if not n:
            return
        res = '1'
        for _ in xrange(n-1):
            i = 1
            curr = res[0]
            new = ''
            count = 1
            while i < len(res):
                if res[i] == curr:
                    count += 1
                else:
                    new += str(count)
                    new += curr
                    curr = res[i]
                    count = 1
                i += 1
            new += str(count)
            new += curr
            res = new
        return res
            
        
s = Solution()
print s.countAndSay(1)
print s.countAndSay(2)
print s.countAndSay(3)
print s.countAndSay(4)
print s.countAndSay(5)
