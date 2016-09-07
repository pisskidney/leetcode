#!/usr/bin/python


class KMP(object):
    def build_table(self, pattern):
        table = [0 for _ in pattern]
        if len(pattern) < 2:
            return table
        i, j = 1, 0
        while i < len(pattern):
            if pattern[i] == pattern[j]:
                table[i] = j + 1
                i += 1
                j += 1
            else:
                if j > 0:
                    j = table[j - 1]
                else:
                    table[i] = 0
                    i += 1
        return table

    def check(self, text, pattern):
        table = self.build_table(pattern)
        it, ip = 0, 0
        found = False
        while it < len(text) and ip < len(pattern):
            if text[it] == pattern[ip]:
                it += 1
                ip += 1
            else:
                if ip > 0:
                    ip = table[ip - 1]
                else:
                    it += 1
            if ip >= len(pattern):
                return it - len(pattern)
        return -1


kmp = KMP()
x = 'abcdabca'
assert kmp.build_table(x) == [0, 0, 0, 0, 1, 2, 3, 1]

x = 'aabaabaaa'
assert kmp.build_table(x) == [0, 1, 0, 1, 2, 3, 4, 5, 2]

t = 'ilikebigbuttsandicannotlie'
p = 'bigb'
assert kmp.check(t, p) == 5

t = 'ilikebigbuttsandicannotlie'
p = 'bigx'
assert kmp.check(t, p) == -1

t = 'abxabcabcaby'
p = 'abcaby'
assert kmp.check(t, p) == 6
