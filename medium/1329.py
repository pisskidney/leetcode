# Given a m * n matrix mat of integers, sort it diagonally in ascending order
# from the top-left to the bottom-right then return the sorted array.


from copy import deepcopy


class Solution():
    def sort(self, mat, i, j):
        # Do a simple count sort
        n, m = len(mat), len(mat[0])
        xi, xj = i, j
        nrs = [0] * 101
        while xi < n and xj < m:
            nrs[mat[xi][xj]] += 1
            xi += 1
            xj += 1
        xi, xj = i, j
        for k in range(101):
            for _ in range(nrs[k]):
                mat[xi][xj] = k
                xi += 1
                xj += 1


    def diagonalSort(self, mat):
        newmat = deepcopy(mat)
        n, m = len(mat), len(mat[0])
        for i in range(n):
            self.sort(newmat, i, 0)
        for j in range(1, m):
            self.sort(newmat, 0, j)
        return newmat


a = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
import numpy as np
print(np.matrix(a))
s = Solution()
print(np.matrix(s.diagonalSort(a)))
