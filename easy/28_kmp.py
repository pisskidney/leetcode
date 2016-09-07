#!/usr/bin/python


class Solution(object):

    def build_table(self, pattern):
        res = [0 for _ in xrange(len(pattern))]
        if len(pattern) < 2:
            return res
        i, j = 1, 0

        while i < len(pattern):
            if pattern[i] == pattern[j]:
                res[i] = j + 1
                i += 1
                j += 1
            else:
                if j > 0:
                    j = res[j-1]
                else:
                    res[i] = 0
                    i += 1
        return res

    def strStr(self, haystack, needle):
        """

        RUNTIME: 109, 59, 118, 72, 92

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

        table = self.build_table(needle)

        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j > 0:
                    j = table[j-1]
                else:
                    i += 1
            if j >= len(needle):
                return i - len(needle) 
        return -1


s = Solution()
x = 'the quick brown fox'
assert s.strStr(x, 'quick') == 4
assert s.strStr(x, 'z') == -1
assert s.strStr(x, 'brown fox') == 10
assert s.strStr(x, 'the quick brown fox') == 0
assert s.strStr('a', 'a') == 0
