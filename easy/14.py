#!/usr/bin/python


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or '' in strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        res = ''
        i = 0
        while 1:
            for j, string in enumerate(strs):
                if i + 1 > len(string):
                    return res
                if j == 0:
                    char = string[i]
                else:
                    if string[i] != char:
                        return res
            res += char
            i += 1
        return res


s = Solution()
print s.longestCommonPrefix(['abcd', 'aba', 'abdsdxxxx'])
