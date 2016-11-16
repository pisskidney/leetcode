#!/usr/bin/python

from collections import defaultdict


class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        h = defaultdict(int)
        for c in p:
            h[p] += 1
        for c in s[:len(p)]:
            if h[c] > 0:
                h[c] -= 1
                count -= 1
        left, right, count = , len(p) - 1, len(p)
        while right < len(s):
            if not count:
                res.append(left)
            right += 1
            if h[right] > 0:
                h[right] -= 1
                count -= 1
            if h[left] >= 0:
                count += 1
                h[left] += 1
            left += 1
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
