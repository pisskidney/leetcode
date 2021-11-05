from typing import List


"""
48. Rotate Image

https://leetcode.com/problems/rotate-image/
"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]
        for i in range(n):
            for j in range(n // 2):
                matrix[j][i], matrix[n-1-j][i] = matrix[n-1-j][i], matrix[j][i]


def main():
    sol = Solution()
    a = [[1, 2], [3, 4]]
    print(a)
    # a = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    sol.rotate(a)
    print(a)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
