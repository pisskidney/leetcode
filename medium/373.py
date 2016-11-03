#!/usr/bin/python


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        for n1 in nums1:
            for n2 in nums2:
                res.append((n1, n2, n1+n2))
        res = sorted(res, key=lambda x: x[2])
        return [(r[0], r[1]) for r in res][:k]


s = Solution()
a = range(100)
b = range(100)
k = 8000
print s.kSmallestPairs(a, b, k)
