#!/usr/bin/python

import collections


class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        h = {}
        if len(s) < len(p):
            return []
        for c in p:
            if c in h:
                h[c] += 1
            else:
                h[c] = 1
        c = 0
        left, right = 0, -1
        while right < len(p)-1:
            right += 1
            if s[right] in h:
                h[s[right]] -= 1
                if h[s[right]] >= 0:
                    c += 1
        if c == len(p):
            res.append(left)
        while right < len(s) - 1:
            if s[left] in h:
                h[s[left]] += 1
                if h[s[left]] > 0:
                    c -= 1
            left, right = left + 1, right + 1
            if s[right] in h:
                h[s[right]] -= 1
                if h[s[right]] >= 0:
                    c += 1
            if c == len(p):
                res.append(left)
        return res


s = Solution()
print s.findAnagrams('abab', 'ab')


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
