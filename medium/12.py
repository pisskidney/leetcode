#!/usr/bin/python


class Solution(object):
    chart = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M',
    }

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        chart = self.chart
        p = 1
        res = ''
        while num > 0:
            current = num % 10
            if current in [1, 2, 3]:
                res = chart[p] * current + res
            elif current == 4:
                res = chart[p] + chart[5*p] + res
            elif current in [5, 6, 7, 8]:
                res = chart[5*p] + chart[p]*(current-5) + res
            elif current == 9:
                res = chart[p] + chart[p*10] + res
            p *= 10
            num /= 10
        return res
        

s = Solution()
print s.intToRoman(3)
print s.intToRoman(5)
print s.intToRoman(7)
print s.intToRoman(9)
print s.intToRoman(317)
