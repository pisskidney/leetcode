#!/usr/bin/python


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = list(s)
        i, j = 0, len(s)-1
        while i < j:
            if res[i] not in 'aeiouAEIOU':
                i += 1
            elif res[j] not in 'aeiouAEIOU':
                j -= 1
            else:
                res[i], res[j] = res[j], res[i]
                i += 1
                j -= 1
        return ''.join(res)


s = Solution()
print s.reverseVowels('leetcode')
