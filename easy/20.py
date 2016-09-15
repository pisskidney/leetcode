#!/usr/bin/python


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        match = {'(': ')', '[': ']', '{': '}'}
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif not stack or match[stack.pop()] != c:
                return False
        return not stack
            

s = Solution()
assert s.isValid('(((') == False
assert s.isValid('}}') == False
assert s.isValid('([)]') == False
assert s.isValid('{()}') == True
