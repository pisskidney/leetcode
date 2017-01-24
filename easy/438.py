#!/usr/bin/python

import collections


class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        left, right = 0, len(right)
        c = collections.defaultdict(int)
            for char in p:
                c[char] += 1
        while right < len(s):
            if right < len(p):

        


        return res


class SolutionRealQuadratic(object):
    def findAnagrams(self, s, p):
        res = []
        h = collections.defaultdict(int)
        for c in p:
            h[c] += 1
        for i in xrange(len(s) - len(p) + 1):
            check = dict(h)
            for j in xrange(len(p)):
                try:
                    check[s[i+j]] -= 1
                    if check[s[i+j]] < 0:
                        break
                except Exception:
                    break
            else:
                res.append(i)
        return res


s = Solution()
print s.findAnagrams('abab', 'ab')


class SolutionQuadratic(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        res = []
        setp = set(p)
        for i in xrange(len(s) - len(p) + 1):
            if set(s[i:i+len(p)]) == setp:
                res.append(i)
        return res
