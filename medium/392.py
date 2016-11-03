#!/usr/bin/python


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        found = True
        for c in s:
            found = False
            while not found and i < len(t):
                if c == t[i]:
                    found = True
                i += 1
        return found


s = Solution()
x = 'dasdasn'
y = ''

print s.isSubsequence(x, y)

            
