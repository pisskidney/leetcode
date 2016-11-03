#!/usr/bin/python


from heapq import heapify, heapreplace


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if len(matrix) is 1:
            return matrix[0][0]
        z = zip(*matrix[1:])
        h = [(matrix[0][i], z[i]) for i in xrange(len(matrix))]
        heapify(h)
        i = 0
        while i < k - 1:
            val, nextval = h[0]
            if nextval:
                heapreplace(h, (nextval[0], nextval[1:]))
            else:
                heappop(h)
            i += 1
        return h[0][0]
                
            
a = [[1,5,10], [4,5,11], [7,8,12]]
s = Solution()
print s.kthSmallest(a, 3)
