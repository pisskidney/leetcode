#!/usr/bin/python


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        h = {}
        a = 0
        b = 0
        for s in secret:
            if s not in h:
                h[s] = 1
            else:
                h[s] += 1
        for i, g in enumerate(guess):
            if g == secret[i]:
                a += 1
                h[g] -= 1
        for g in guess:
            if g in h and h[g] >= 1:
                b += 1
                h[g] -= 1
        return '%dA%dB' % (a, b)

