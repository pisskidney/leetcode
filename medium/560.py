"""
560. Subarray Sum Equals K

https://leetcode.com/problems/subarray-sum-equals-k/
"""
from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        summ = 0
        h = defaultdict(int)
        h[0] = 1
        for num in nums:
            summ += num
            res += h[summ-k]
            h[summ] += 1
        return res


def main():
    s = Solution()
    print(s.subarraySum([1, 2, -1, -2], 1))


if __name__ == '__main__':
    raise(SystemExit(main()))
