#!/usr/bin/python


class Solution(object):
    def strStr(self, haystack, needle):
        """

        RUNTIME: 59, 65, 49, 65, 38

        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) > len(haystack):
            return -1
        if not needle:
            return 0
        if not haystack:
            return -1

        for i in xrange(len(haystack)-len(needle)+1):
            found = True
            for j in xrange(len(needle)):
                if haystack[i+j] != needle[j]:
                    found = False
                    break
            if found:
                return i
        return -1


s = Solution()
x = 'the quick brown fox'
assert s.strStr(x, 'quick') == 4
assert s.strStr(x, 'z') == -1
assert s.strStr(x, 'brown fox') == 10
assert s.strStr(x, 'the quick brown fox') == 0
assert s.strStr('a', 'a') == 0
