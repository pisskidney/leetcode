#!/usr/bin/python


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.binary(1, n)
    
    def binary(self, left, right):
        print left, right
        if left == right:
            return left
        mid = (left + right) / 2
        if (isBadVersion(mid)):
            return self.binary(left, mid)
        else:
            return self.binary(mid + 1, right)
            
def isBadVersion(x):
    if x >= 10:
        return True
    else:
        return False

s = Solution()

print s.firstBadVersion(22)
