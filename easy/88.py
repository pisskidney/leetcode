#!/usr/bin/python


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 or m == 0:
            nums1[:] = nums2
            return 
        if not nums2 or n == 0:
            return
        i, j = 0, 0
        print 'len: ', m, n
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                i += 1
            else:
                nums1[:] = nums1[:i] + [nums2[j]] + nums1[i:]
                i += 1
                j += 1
                m += 1
        if j < n:
            nums1[:] += nums2[j:]


s = Solution()
y = [1, 3, 5, 7, 8, 9, 10]
x = []
s.merge(x, len(x), y, len(y))
print x

