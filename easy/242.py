"""
242. Valid Anagram

https://leetcode.com/problems/valid-anagram/
"""


from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = defaultdict(int)
        for c in s:
            a[c] += 1
        for c in t:
            if c not in a or a[c] == 0:
                return False
            a[c] -= 1
        if any(a.values()):
            return False
        return True


def main():
    s = Solution()
    print(s.xxx())


if __name__ == '__main__':
    raise(SystemExit(main()))
