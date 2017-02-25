#!/usr/bin/python


class Solution(object):
    def reverseWords(self, s):
        if s == '':
            return s
        res = []
        i = len(s) - 2
        while i >= -1:
            if s[i] == ' ' or i == -1:
                word = ''
                j = i + 1
                while j < len(s) and s[j] != ' ':
                    word += s[j]
                    j += 1
                if word:
                    res.append(word)
            i -= 1
        return ' '.join(res)


s = Solution()
print s.reverseWords('a x')

