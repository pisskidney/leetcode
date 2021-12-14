"""
136. Single Number

https://leetcode.com/problems/single-number/
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res


def main():
    s = Solution()
    print(s.xxx())


if __name__ == '__main__':
    raise(SystemExit(main()))
