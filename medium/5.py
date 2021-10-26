#!/usr/bin/python


"""
5. Longest Palindromic Substring

https://leetcode.com/problems/longest-palindromic-substring/
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        if len(s) == 1:
            return s
        if len(s) == 2:
            return s[0] if s[0] != s[1] else s

        longest = s[0]
        for i in range(len(s) * 2 - 3):
            current = 0 if i % 2 == 0 else 1
            for j in range(min(i // 2 + 1, len(s) - (((i + 1) // 2) + 1))):
                left = i // 2 - j
                right = ((i + 1) // 2) + 1 + j
                if s[left] == s[right]:
                    current += 2
                    if current > len(longest):
                        longest = s[left:right+1]
                else:
                    break
        return longest


def main():
    sol = Solution()
    print(sol.longestPalindrome('babad'))
    print(sol.longestPalindrome('cbbd'))
    print(sol.longestPalindrome('ac'))
    print(sol.longestPalindrome('aacabdkacaa'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
