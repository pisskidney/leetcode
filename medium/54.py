#!/usr/bin/python


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        res = []
        m, n = len(matrix), len(matrix[0])
        step = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        count = 0
        top, bottom, left, right = -1, m, -1, n
        i, j = 0, 0
        k = 0
        while count < m * n:
            if j >= right:
                i += 1
                j -= 1 
                top += 1
                k += 1
            elif i >= bottom:
                i -= 1
                j -= 1
                right -= 1
                k += 1 
            elif j <= left:
                i -= 1
                j += 1
                bottom -= 1
                k += 1
            elif i <= top:
                i += 1
                j += 1
                left += 1
                k += 1
            k %= 4
            res.append(matrix[i][j])
            i += step[k][0]
            j += step[k][1]
            count += 1
        return res

a = [[1,2,3], [4,5,6], [7,8,9]]
s = Solution()
print s.spiralOrder(a)
