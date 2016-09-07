#!/usr/bin/python

class Solution(object):
    def isPalindrome(self, s):

        if len(s) <= 1:
            return True

        left = 0
        right = len(s) - 1
        isPali = True
        while isPali and left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                isPali = False
            left += 1
            right -= 1

        return isPali


s = Solution()

assert s.isPalindrome('')
assert s.isPalindrome('a')
assert s.isPalindrome('bB')
assert s.isPalindrome('!geza Kek@@ az% EG..')
assert s.isPalindrome('a race car') == False
assert s.isPalindrome('baa0 0aaB')
