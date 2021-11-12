#!/usr/bin/python
import math


"""
60. Permutation Sequence

https://leetcode.com/problems/permutation-sequence/
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        res = []
        nums = list(range(1, n + 1))

        def go(nums, k):
            if not nums:
                return
            n = len(nums)
            total = math.factorial(n)
            segment = total // n
            place = (k - 1) // segment
            res.append(nums[place])
            go(nums[:place] + nums[place+1:], k - segment * place)

        go(nums, k)
        return ''.join(map(str, res))


def main():
    sol = Solution()
    # print(sol.getPermutation(9, 600))
    print(sol.getPermutation(4, 6))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())


'''
1234
1243
1324
1342
1423
1432
2134
2143
2314
2341
2413
2431
'''
