#!/usr/bin/python


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not pattern and not str:
            return True
        if not pattern or not str:
            return False
        str_list = str.split()
        if len(str_list) != len(pattern):
            return False
        h1 = {}
        h2 = {}
        for i, word in enumerate(str_list):
            if word not in h1:
                h1[word] = pattern[i]
            elif h1[word] != pattern[i]:
                return False
            if pattern[i] not in h2:
                h2[pattern[i]] = word
            elif h2[pattern[i]] != word:
                return False
        return True


s = Solution()
assert s.wordPattern('aaaa', 'cat cat cat cat') == True
assert s.wordPattern('xaaa', 'dog cat cat cat') == True
assert s.wordPattern('abba', 'cat dogg dogg cat') == True
assert s.wordPattern('aaca', 'cat cat car cat') == True
assert s.wordPattern('acca', 'cat cat car cat') == False
assert s.wordPattern('aaa', 'cat cat cat cat') == False
assert s.wordPattern('abba', 'dog cat cat fish') == False
