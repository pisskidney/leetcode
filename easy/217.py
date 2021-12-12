"""
217. Contains Duplicate

https://leetcode.com/problems/contains-duplicate/
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set([])
        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        return False


def main():
    s = Solution()
    print(s.xxx())


if __name__ == '__main__':
    raise(SystemExit(main()))
