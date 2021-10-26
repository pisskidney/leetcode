#!/usr/bin/python


"""
3. Longest Substring Without Repeating Characters

https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        seen = {}
        for right, c in enumerate(s):
            if c in seen and seen[c] >= left:
                left = seen[c] + 1
            seen[c] = right
            longest = max(longest, right - left + 1)
        return longest


def main():
    sol = Solution()
    print(sol.lengthOfLongestSubstring('amtortiamzx'))
    print(sol.lengthOfLongestSubstring('abcabcbb'))
    print(sol.lengthOfLongestSubstring('bbtablud'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
