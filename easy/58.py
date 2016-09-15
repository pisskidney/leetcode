#!/usr/bin/python


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        i = len(s) - 1
        found = False
        last_char = None
        while i >= 0:
            if s[i] == ' ':
                if found:
                    return last_char - i
            else:
                if not last_char:
                    last_char = i
                found = True
            i -= 1
        if found:
            return last_char + 1
        return 0


s = Solution()
print s.lengthOfLastWord('ffs ffs  lol55   ')
print s.lengthOfLastWord('lol55')
print s.lengthOfLastWord('a a')
print s.lengthOfLastWord(' ')
        
