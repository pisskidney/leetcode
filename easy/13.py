"""
13. Roman to Integer

https://leetcode.com/problems/roman-to-integer/
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        res = roman[s[-1]]
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res


def main():
    s = Solution()
    print(s.romanToInt('MCMXCIV'))


if __name__ == '__main__':
    raise(SystemExit(main()))
