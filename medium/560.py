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
        cumsum = []
        h = defaultdict(int)
        for num in nums:
            summ += num
            cumsum.append(summ)
        for num in cumsum:
            res += h[num-k]
            h[num] += 1
        return res


def main():
    s = Solution()
    print(s.subarraySum([1, 2, -1, -2], 1))


if __name__ == '__main__':
    raise(SystemExit(main()))
