"""
9. Palindrome Number

https://leetcode.com/problems/palindrome-number/
"""
import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        n = int(math.log10(x)) + 1
        for i in range(n // 2):
            temp = x // (10 ** i)
            r = temp % 10
            temp = x // (10 ** (n - i - 1))
            l = temp % 10
            print(n)
            if l != r:
                return False
        return True


def main():
    s = Solution()
    print(s.isPalindrome(1000))


if __name__ == '__main__':
    raise(SystemExit(main()))
