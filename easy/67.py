#!/usr/bin/python


class Solution(object):
    def addBinary(self, aa, bb):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        lena = len(aa); lenb = len(bb);
        maxlen = lena if lena > lenb else lenb
        carry = False
        for i in xrange(maxlen):
            a = False
            b = False
            newcarry = False
            if lena - i - 1 >= 0 and aa[lena-i-1] == '1':
                a = True
            if lenb - i - 1 >= 0 and bb[lenb-i-1] == '1':
                b = True
            if (a and b):
                if carry:
                    res = '1' + res
                else:
                    res = '0' + res
                newcarry = True
            elif (a != b):
                if carry:
                    res = '0' + res
                    newcarry = True
                else:
                    res = '1' + res
            else:
                if carry:
                    res = '1' + res
                else:
                    res = '0' + res
            carry = newcarry
        if carry:
            res = '1' + res

        return res
