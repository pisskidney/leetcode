"""
74. Search a 2D Matrix

https://leetcode.com/problems/search-a-2d-matrix/
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        i = j = 0
        while i < n and j < m and matrix[i][j] <= target:
            if matrix[i][j] == target:
                return True
            elif (i + 1 < n and matrix[i+1][j] <= target):
                i += 1
            else:
                j += 1
        return False


def main():
    sol = Solution()
    print(sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
    print(sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
    print(sol.searchMatrix([[1]], 2))
    print(sol.searchMatrix([[1]], 1))
    print(sol.searchMatrix([[1]], 0))
    print(sol.searchMatrix([[1], [2], [3], [5]], 4))
    print(sol.searchMatrix([[1], [2], [3], [5]], 5))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
